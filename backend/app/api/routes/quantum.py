from fastapi import APIRouter

router = APIRouter(prefix="/quantum", tags=["quantum"])


@router.get("/status")
async def quantum_status():
    return {
        "backend": "simulator",
        "qubits": 4,
        "depth": 3,
        "shots": 1024,
        "mode": "simulation",
        "note": "This is a simulator, not real hardware execution."
    }
