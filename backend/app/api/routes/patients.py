from fastapi import APIRouter

router = APIRouter(prefix="/patients", tags=["patients"])


@router.get("/")
async def list_patients():
    return {
        "patients": [
            {"id": 1, "name": "Aarav Sharma", "age": 32, "status": "active"},
            {"id": 2, "name": "Meera Patel", "age": 41, "status": "screening"},
        ]
    }


@router.get("/{patient_id}")
async def patient_detail(patient_id: int):
    return {"id": patient_id, "name": "Sample Patient", "risk_level": "elevated"}
