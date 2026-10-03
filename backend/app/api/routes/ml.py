from fastapi import APIRouter

router = APIRouter(prefix="/ml", tags=["ml"])


@router.get("/overview")
async def overview():
    return {
        "models": ["Logistic Regression", "Random Forest", "SVM"],
        "supported_metrics": ["Accuracy", "Precision", "Recall", "F1", "ROC-AUC", "Confusion Matrix"],
        "status": "ready"
    }
