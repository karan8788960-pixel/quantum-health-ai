from fastapi import APIRouter

router = APIRouter(prefix="/fairness", tags=["fairness"])


@router.get("/summary")
async def fairness_summary():
    return {
        "groups": ["Group A", "Group B"],
        "status": "demographic comparison where data exists",
        "warning": "Fairness is only assessed when relevant data is available."
    }
