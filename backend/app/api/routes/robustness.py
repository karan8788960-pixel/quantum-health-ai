from fastapi import APIRouter

router = APIRouter(prefix="/robustness", tags=["robustness"])


@router.get("/tests")
async def robustness_tests():
    return {
        "tested_conditions": ["clean data", "noisy data", "missing features", "feature perturbations"],
        "status": "real experiments only",
    }
