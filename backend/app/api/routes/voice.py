from fastapi import APIRouter

router = APIRouter(prefix="/voice", tags=["voice"])


@router.get("/status")
async def voice_status():
    return {
        "state": "Permission Required",
        "message": "Microphone access requires explicit user permission.",
        "quality": "unavailable",
    }


@router.post("/record")
async def voice_record(payload: dict):
    return {
        "status": "Processing",
        "signal_quality": 0.82,
        "features": {
            "pitch": 172.4,
            "amplitude": 0.91,
            "speech_rate": 2.5,
            "jitter": 0.04,
            "shimmer": 0.08,
        },
        "safety":"No raw audio is stored by default; derived features are used."
    }
