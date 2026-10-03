from fastapi import APIRouter

router = APIRouter(prefix="/motion", tags=["motion"])


@router.get("/status")
async def motion_status():
    return {
        "state": "Unavailable",
        "message": "Motion sensors are unavailable on this device/browser.",
        "sensor_availability": "unavailable",
    }
