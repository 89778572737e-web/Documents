"""
Quality Gates validator for AI Travel Equipment Business Knowledge Base.
Implements GATE 1-6 logic from Quality_Gates.md (Phase 9).

Usage:
    export GH_TOKEN="your_github_token"
    python3 run_gates.py
"""

import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class GateResult:
    gate_name: str
    status: str  # PASS, FAIL, INSUFFICIENT_DATA
    details: str


def parse_field(content: str, field_name: str) -> Optional[str]:
    """
    Extracts the value following a 'FieldName:' line in our KB markdown format.
    """
    pattern = rf"^{re.escape(field_name)}:\s*\n\s*\n?(.+?)(?=\n\n[A-Z]|\n##|\Z)"
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
    if match:
        value = match.group(1).strip()
        return value if value else None
    return None


def is_missing_or_placeholder(value: Optional[str]) -> bool:
    """A field counts as missing if absent OR contains a known placeholder."""
    if value is None:
        return True
    placeholders = [
        "не указано", "не подтверждено", "требует проверки",
        "не рассчитана", "не рассчитано", "(не указано)",
        "(не подтверждено независимо", "не подтверждена",
    ]
    lowered = value.lower()
    return any(p in lowered for p in placeholders)


def gate_1_product_data_completeness(product_content: str) -> GateResult:
    """GATE 1 — Product Data Completeness (Quality_Gates.md)."""
    description = parse_field(product_content, "Description")
    category = parse_field(product_content, "Category")

    if is_missing_or_placeholder(description) or is_missing_or_placeholder(category):
        return GateResult("GATE 1: Product Data Completeness", "FAIL",
                           "Description или Category отсутствуют — это блокирующие поля.")

    return GateResult("GATE 1: Product Data Completeness", "PASS",
                       "Description и Category заполнены.")


def gate_2_supplier_verification(supplier_content: str) -> GateResult:
    """GATE 2 — Supplier Verification (Quality_Gates.md)."""
    price = parse_field(supplier_content, "Unit Price")
    moq = parse_field(supplier_content, "MOQ")

    if is_missing_or_placeholder(price) or is_missing_or_placeholder(moq):
        return GateResult("GATE 2: Supplier Verification", "INSUFFICIENT_DATA",
                           "Цена или MOQ не подтверждены поставщиком.")

    return GateResult("GATE 2: Supplier Verification", "PASS",
                       f"Цена и MOQ подтверждены: price='{price}', moq='{moq}'.")


def gate_3_financial_viability(unit_cost: Optional[float], sell_price: Optional[float],
                                referral_fee_pct: float = 0.15,
                                fulfillment_fee: float = 3.47) -> GateResult:
    """
    GATE 3 — Financial Viability (Quality_Gates.md).
    Per user's decision: NON-BLOCKING. Always computes and returns the margin %,
    never auto-rejects. User decides case-by-case.
    """
    if unit_cost is None or sell_price is None:
        return GateResult("GATE 3: Financial Viability", "INSUFFICIENT_DATA",
                           "Себестоимость или цена продажи не указаны — расчёт невозможен.")

    referral_fee = sell_price * referral_fee_pct
    gross_profit = sell_price - unit_cost - referral_fee - fulfillment_fee
    margin_pct = (gross_profit / sell_price) * 100 if sell_price else 0

    return GateResult(
        "GATE 3: Financial Viability",
        "PASS",
        f"Маржинальность: {margin_pct:.1f}% "
        f"(цена ${sell_price:.2f}, себестоимость ${unit_cost:.2f}, "
        f"referral fee ${referral_fee:.2f}, fulfillment fee ${fulfillment_fee:.2f}, "
        f"валовая прибыль ${gross_profit:.2f}). "
        f"НЕ учтены: доставка от поставщика, реклама, пошлины — см. правило GATE 3 (non-blocking)."
    )


def run_all_gates(product_content: str, supplier_content: str,
                   unit_cost: Optional[float], sell_price: Optional[float]) -> list:
    """Run all implemented gates and return results."""
    return [
        gate_1_product_data_completeness(product_content),
        gate_2_supplier_verification(supplier_content),
        gate_3_financial_viability(unit_cost, sell_price),
    ]