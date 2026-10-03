from fastapi import APIRouter

router = APIRouter(prefix="/features", tags=["features"])


@router.get("/fusion")
async def feature_fusion():
    return {
        "strategy": "late multimodal fusion with quality-weighted feature normalization and PCA",
        "supports": ["symptoms", "voice", "camera", "accelerometer", "gyroscope"],
        "status": "documented"
    }
