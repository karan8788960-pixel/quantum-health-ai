from fastapi import APIRouter

router = APIRouter(prefix="/experiments", tags=["experiments"])


@router.get("/")
async def get_experiments():
    return {"experiments": [{"id": "EXP-001", "model": "Hybrid QML", "status": "completed"}]}
