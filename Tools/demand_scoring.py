"""
Demand Scoring Engine — implements the Early Signal Score formula
from Demand_Validation_Agent/README.md (Phase 12 design).

This is REAL, TESTABLE math logic. It has NOT yet been run on real
experiment data (no accounts/API connected) — tested here with
SYNTHETIC example data to prove the formula works correctly.
"""
from dataclasses import dataclass
from typing import List


@dataclass
class MetricSnapshot:
    views: int
    likes: int
    comments: int
    shares: int
    hours_since_publish: float


def percentile_rank(value: float, cohort_values: List[float]) -> float:
    """
    Returns what percentile `value` falls at within `cohort_values`.
    This is the core anti-pattern-avoidance from our design: NEVER use
    absolute thresholds (e.g. "1000 views = good"), always relative
    to a comparable cohort (same platform/category/account/age).
    """
    if not cohort_values:
        return 50.0  # no cohort data yet — neutral default
    below_or_equal = sum(1 for v in cohort_values if v <= value)
    return (below_or_equal / len(cohort_values)) * 100


def compute_early_signal_score(
    view_velocity_percentile: float,
    engagement_velocity_percentile: float,
    share_comment_quality_percentile: float,
    retention_signal_percentile: float,
) -> float:
    """
    EarlySignalScore formula from Demand_Validation_Agent/README.md:
        0.35 × ViewVelocityPercentile
      + 0.25 × EngagementVelocityPercentile
      + 0.20 × ShareCommentQualityPercentile
      + 0.20 × Retention/ContinuationSignal

    NOTE: weights are an explicitly-flagged STARTING HYPOTHESIS in the
    original design, not validated — see open questions in the agent contract.
    """
    return (
        0.35 * view_velocity_percentile +
        0.25 * engagement_velocity_percentile +
        0.20 * share_comment_quality_percentile +
        0.20 * retention_signal_percentile
    )


def classify_demand(early_signal_score: float, calibration_status: str = "pending") -> dict:
    """
    Returns confirmed / weak / insufficient_data + confidence,
    per Demand_Validation_Agent/README.md and GATE 5 (Quality_Gates.md).
    """
    if calibration_status != "validated":
        # Per design: if Tier-A→Tier-B correlation hasn't been calibrated,
        # results are screening evidence only, not a final verdict.
        confidence_cap = 0.5
    else:
        confidence_cap = 1.0

    if early_signal_score >= 80:
        classification = "confirmed"
        confidence = min(0.85, confidence_cap)
    elif early_signal_score >= 50:
        classification = "weak"
        confidence = min(0.6, confidence_cap)
    else:
        classification = "insufficient_data"
        confidence = min(0.4, confidence_cap)

    return {
        "classification": classification,
        "confidence": confidence,
        "early_signal_score": early_signal_score,
        "calibration_status": calibration_status,
        "note": "confidence capped at 0.5 because calibration_status != validated"
                if calibration_status != "validated" else None,
    }


if __name__ == "__main__":
    print("=" * 60)
    print("DEMONSTRATION WITH SYNTHETIC DATA (no real experiments exist yet)")
    print("=" * 60)

    # Synthetic cohort: 20 hypothetical past experiments' view velocities
    synthetic_cohort_view_velocity = [50, 80, 120, 45, 200, 90, 60, 300, 150, 70,
                                        40, 110, 95, 130, 55, 220, 85, 65, 175, 100]

    # A new candidate experiment
    candidate_view_velocity = 210  # views/hour

    vv_percentile = percentile_rank(candidate_view_velocity, synthetic_cohort_view_velocity)
    print(f"\nCandidate view velocity: {candidate_view_velocity}/hr")
    print(f"Percentile within synthetic cohort of 20: {vv_percentile:.1f}")

    # Assume other percentiles for this synthetic example
    score = compute_early_signal_score(
        view_velocity_percentile=vv_percentile,
        engagement_velocity_percentile=72,
        share_comment_quality_percentile=68,
        retention_signal_percentile=80,
    )
    print(f"\nEarly Signal Score: {score:.1f}")

    result = classify_demand(score, calibration_status="pending")
    print(f"\nClassification result: {result}")