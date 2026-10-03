from fastapi import APIRouter

router = APIRouter(prefix="/sensors", tags=["sensors"])


@router.get("/status")
async def sensor_status():
    return {
        "calibration": "ready",
        "availability": "unavailable",
        "message": "Sensor unavailable."
    }
