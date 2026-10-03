from fastapi import APIRouter

router = APIRouter(prefix="/explainability", tags=["explainability"])


@router.get("/summary")
async def explainability_summary():
    return {
        "title": "WHY DID THE MODEL PRODUCE THIS RESULT?",
        "important_features": ["symptom severity", "voice stability", "movement regularity"],
        "uncertainty": 0.31,
        "data_quality": "acceptable",
    }
