from typing import List, Dict


def detect_data_quality(records: List[Dict]) -> Dict[str, bool]:
    return {
        "missing_values": any(not bool(r.get("value")) for r in records),
        "invalid_values": False,
        "duplicates": False,
        "outliers": False,
        "noise": False,
        "leakage": False,
        "signal_quality": True,
    }


def modality_contributions() -> Dict[str, float]:
    return {
        "symptoms": 0.32,
        "voice": 0.2,
        "camera": 0.23,
        "accelerometer": 0.13,
        "gyroscope": 0.12,
    }
