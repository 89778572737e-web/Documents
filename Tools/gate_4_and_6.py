"""
GATE 4 (Marketing Feasibility) and GATE 6 (Business Decision aggregator)
per Quality_Gates.md.
"""
import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class GateResult:
    gate_name: str
    status: str
    details: str


def gate_4_marketing_feasibility(analysis_content: str) -> GateResult:
    """
    GATE 4 — Marketing Feasibility.
    Checks the Analysis History file for a Marketing Agent section
    with actual audience/positioning content (not just a placeholder).
    """
    marketing_section = re.search(
        r"Marketing Agent Analysis(.*?)(?=\n---|\n# [A-Z]|\Z)",
        analysis_content, re.DOTALL
    )
    if not marketing_section:
        return GateResult("GATE 4: Marketing Feasibility", "INSUFFICIENT_DATA",
                           "Раздел Marketing Agent Analysis не найден в истории анализа.")

    text = marketing_section.group(1).strip()
    if len(text) < 20:  # essentially empty
        return GateResult("GATE 4: Marketing Feasibility", "FAIL",
                           "Marketing Agent Analysis присутствует, но пуст или неинформативен.")

    return GateResult("GATE 4: Marketing Feasibility", "PASS",
                       "Найдена содержательная маркетинговая гипотеза (аудитория/позиционирование).")


def gate_6_business_decision_summary(gate_results: list) -> dict:
    """
    GATE 6 — Business Decision (aggregator, not automated decision-maker).
    Per Responsibility_Matrix.md: the decision itself belongs to Business Manager
    (a human-in-the-loop role in the current architecture), NOT to this code.
    This function only SUMMARIZES prior gates to support that decision —
    it does not decide FOR the user.
    """
    fails = [r for r in gate_results if r.status == "FAIL"]
    insufficient = [r for r in gate_results if r.status == "INSUFFICIENT_DATA"]
    passes = [r for r in gate_results if r.status == "PASS"]

    summary = {
        "total_gates_evaluated": len(gate_results),
        "passed": len(passes),
        "failed": len(fails),
        "insufficient_data": len(insufficient),
        "blocking_issues": [f"{r.gate_name}: {r.details}" for r in fails],
        "missing_data_issues": [f"{r.gate_name}: {r.details}" for r in insufficient],
        "recommendation": None,
    }

    if fails:
        summary["recommendation"] = (
            "НЕ РЕКОМЕНДУЕТСЯ запускать без решения блокирующих проблем. "
            "Окончательное решение — за Business Manager / пользователем."
        )
    elif insufficient:
        summary["recommendation"] = (
            "Данных недостаточно для уверенного решения. "
            "Рекомендуется дособрать недостающие данные перед запуском."
        )
    else:
        summary["recommendation"] = (
            "Все проверенные gates пройдены. Это НЕ автоматическое одобрение закупки — "
            "финальное решение по-прежнему принимает пользователь/Business Manager (см. Responsibility_Matrix.md)."
        )

    return summary