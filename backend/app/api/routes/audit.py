from fastapi import APIRouter

router = APIRouter(prefix="/audit", tags=["audit"])


@router.get("/")
async def audit_events():
    return {"events": [{"type": "login", "actor": "doctor", "status": "success"}]}
