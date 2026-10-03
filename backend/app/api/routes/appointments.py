from fastapi import APIRouter

router = APIRouter(prefix="/appointments", tags=["appointments"])


@router.get("/")
async def appointments():
    return {"appointments": [{"id": 1, "doctor": "Dr. Nair", "time": "2026-10-04T10:00:00Z", "status": "scheduled"}]}
