"""
Runs ALL implemented Quality Gates against the REAL current Knowledge Base
and produces one consolidated health report. This is the closest thing
to an automated "system status check" that exists in the project so far.

Usage:
    export GH_TOKEN="your_github_token"
    python3 run_full_audit.py
"""
import os
import re
import subprocess
import json
import base64
import sys

sys.path.insert(0, os.path.dirname(__file__))
from quality_gates import run_all_gates, gate_1_product_data_completeness, gate_2_supplier_verification, gate_3_financial_viability
from gate_4_and_6 import gate_4_marketing_feasibility, gate_6_business_decision_summary

REPO = "89778572737e-web/Documents"


def fetch_file(path):
    token = os.environ.get("GH_TOKEN")
    if not token:
        raise RuntimeError("Set GH_TOKEN environment variable before running this script.")
    result = subprocess.run(
        ['curl', '-s', '-H', f'Authorization: Bearer {token}',
         '-H', 'Accept: application/vnd.github+json',
         f'https://api.github.com/repos/{REPO}/contents/{path}?ref=main'],
        capture_output=True, text=True
    )
    data = json.loads(result.stdout)
    if 'content' not in data:
        return None  # file doesn't exist
    return base64.b64decode(data['content']).decode('utf-8')


def split_records(content, prefix):
    """Разбивает файл на отдельные записи по заголовкам '# Prefix-XXXX'. Возвращает {ID: текст записи}."""
    parts = re.split(rf"(?m)^# ({prefix}-\d{{4}})\s*$", content)
    return {parts[i]: parts[i + 1] for i in range(1, len(parts) - 1, 2)}


def supplier_id_of(product_record):
    m = re.search(r"Supplier ID:\s*(Supplier-\d{4})", product_record)
    return m.group(1) if m else None


def find_product_ids(products_content):
    return sorted(set(re.findall(r"Product-\d{4}", products_content)))


def parse_gate3_input(analysis_content):
    """Читает из файла анализа строку вида:
    GATE3_INPUT: unit_cost=3.50 sell_price=25.00
    (цена продажи — предположение, оно описано в самом анализе)."""
    import re
    m = re.search(r"(?m)^GATE3_INPUT:\s*unit_cost=([\d.]+)\s+sell_price=([\d.]+)", analysis_content or "")
    if not m:
        return {}
    return {"unit_cost": float(m.group(1)), "sell_price": float(m.group(2))}


if __name__ == "__main__":
    print("=" * 70)
    print("FULL KNOWLEDGE BASE AUDIT — run_full_audit.py")
    print("=" * 70)

    products_content = fetch_file('Knowledge_Base/Products.md')
    suppliers_content = fetch_file('Knowledge_Base/Suppliers.md')

    product_ids = find_product_ids(products_content)
    print(f"\nНайдено товаров в базе: {len(product_ids)} — {product_ids}")

    # Real financial inputs for Product-0001 (from our Financial Evaluation)
    known_financials = {
        "Product-0001": {"unit_cost": 3.75, "sell_price": 25.00}
    }

    product_records = split_records(products_content, "Product")
    supplier_records = split_records(suppliers_content, "Supplier")

    for pid in product_ids:
        print(f"\n{'-' * 70}")
        print(f"АУДИТ: {pid}")
        print('-' * 70)

        analysis_content = fetch_file(f'Knowledge_Base/_Analysis/{pid}_Analysis.md') or ""

        financials = known_financials.get(pid) or parse_gate3_input(analysis_content)
        gates = [
            gate_1_product_data_completeness(product_records.get(pid, "")),
            gate_2_supplier_verification(supplier_records.get(supplier_id_of(product_records.get(pid, "")), "")),
            gate_3_financial_viability(financials.get("unit_cost"), financials.get("sell_price")),
            gate_4_marketing_feasibility(analysis_content),
        ]

        for g in gates:
            print(f"  [{g.status}] {g.gate_name}")
            print(f"      {g.details}")

        summary = gate_6_business_decision_summary(gates)
        print(f"\n  ИТОГ: {summary['passed']}/{summary['total_gates_evaluated']} gates пройдено.")
        print(f"  РЕКОМЕНДАЦИЯ: {summary['recommendation']}")

    print(f"\n{'=' * 70}")
    print("Аудит завершён. Напоминание: это диагностика, а не автоматическое")
    print("решение о закупке — финальное решение принимает пользователь/Business Manager.")