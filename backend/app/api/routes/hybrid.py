from fastapi import APIRouter

router = APIRouter(prefix="/hybrid", tags=["hybrid"])


@router.get("/status")
async def hybrid_status():
    return {
        "pipeline": [
            "Classical preprocessing",
            "Feature selection",
            "PCA",
            "Quantum feature encoding",
            "Quantum circuit",
            "Classical optimizer",
            "Prediction",
        ],
        "status": "central SIH26139 feature"
    }
