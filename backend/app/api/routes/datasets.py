from fastapi import APIRouter

router = APIRouter(prefix="/datasets", tags=["datasets"])


@router.get("/")
async def datasets():
    return {"datasets": [{"id": 1, "name": "Demo Clinical Screening", "status": "available"}]}
