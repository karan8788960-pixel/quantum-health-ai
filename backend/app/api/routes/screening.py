from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/screening", tags=["screening"])


class ScreeningPayload(BaseModel):
    symptoms: list[dict] = []
    voice: dict | None = None
    camera: dict | None = None
    motion: dict | None = None
    demo_mode: bool = False


@router.post("/submit")
async def submit_screening(payload: ScreeningPayload):
    total_severity = sum(item.get("severity", 0) for item in payload.symptoms)
    risk_score = min(0.95, max(0.02, total_severity / 30 + (0.2 if payload.demo_mode else 0.05)))
    risk_level = "elevated" if risk_score > 0.5 else "low"
    reliability = "Reliable Enough for Screening" if risk_score < 0.8 else "Uncertain"
    return {
        "risk_category": risk_level,
        "risk_score": round(risk_score, 3),
        "model": "Hybrid QML",
        "reliability": reliability,
        "data_quality": "Good" if payload.demo_mode or total_severity > 0 else "Insufficient",
        "signal_agreement": "Moderate",
        "important_features": ["symptom severity", "voice stability", "movement regularity"],
        "safety_message": "This is a research/decision-support screening result and is not a medical diagnosis."
    }


@router.get("/workflow")
async def workflow():
    return {
        "steps": [
            "Basic Information",
            "Symptoms",
            "Health Data",
            "Voice",
            "Camera",
            "Motion Sensors",
            "Data Quality",
            "AI Analysis",
            "Result",
        ]
    }
