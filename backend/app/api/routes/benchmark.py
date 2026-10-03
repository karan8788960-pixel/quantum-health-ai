from fastapi import APIRouter

router = APIRouter(prefix="/benchmark", tags=["benchmark"])


@router.get("/")
async def benchmark_summary():
    return {
        "title": "QUANTUM ADVANTAGE REALITY CHECK",
        "models": [
            {"name": "Classical ML", "accuracy": 0.84},
            {"name": "Quantum ML", "accuracy": 0.86},
            {"name": "Hybrid QML", "accuracy": 0.91},
        ],
        "note": "Measured results may vary by dataset and preprocessing pipeline."
    }
