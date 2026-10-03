from fastapi import APIRouter

router = APIRouter(prefix="/preprocessing", tags=["preprocessing"])


@router.get("/pipeline")
async def preprocessing_pipeline():
    return {
        "pipeline": [
            "Raw Inputs",
            "Quality Check",
            "Feature Extraction",
            "Feature Normalization",
            "Feature Selection",
            "PCA",
            "Multimodal Fusion",
            "Classical ML",
            "Quantum ML",
            "Hybrid QML",
        ]
    }
