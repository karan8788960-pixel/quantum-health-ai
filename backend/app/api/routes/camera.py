from fastapi import APIRouter

router = APIRouter(prefix="/camera", tags=["camera"])


@router.get("/status")
async def camera_status():
    return {
        "state": "Ready",
        "message": "Camera access is requested only after user action.",
        "tracking": "available",
    }


@router.post("/analyze")
async def camera_analyze(payload: dict):
    return {
        "status": "Completed",
        "signal_quality": 0.78,
        "features": {
            "amplitude": 0.66,
            "velocity": 0.58,
            "acceleration": 0.47,
            "smoothness": 0.72,
        },
        "warning": "Unable to obtain reliable movement data. Please repeat the test."
    }
