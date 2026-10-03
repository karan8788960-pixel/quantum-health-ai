from typing import Dict, Any


def build_reliability_summary(data_quality: Dict[str, Any], signal_agreement: str, uncertainty: float) -> str:
    if data_quality.get("missing_values") or data_quality.get("invalid_values"):
        return "Insufficient Evidence"
    if uncertainty > 0.75:
        return "Uncertain"
    if signal_agreement == "Poor":
        return "Outside Model Domain"
    return "Reliable Enough for Screening"
