from fastapi import APIRouter

router = APIRouter(prefix="/reports", tags=["reports"])


@router.get("/sample")
async def sample_report():
    return {
        "title": "Research Screening Report",
        "sections": ["Dataset", "Preprocessing", "Classical Model", "QML Model", "Hybrid Model", "Reliability"],
        "status": "ready"
    }
