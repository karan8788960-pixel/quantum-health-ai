from typing import Optional, List
from pydantic import BaseModel, Field


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class LoginRequest(BaseModel):
    username: str
    password: str


class UserCreate(BaseModel):
    username: str
    email: str
    full_name: str
    password: str
    role: str = "patient"


class PatientCreate(BaseModel):
    first_name: str
    last_name: str
    age: Optional[int] = None
    sex: Optional[str] = None
    medical_history: str = ""


class SymptomInput(BaseModel):
    name: str
    severity: int = Field(default=1, ge=0, le=10)
    duration_days: int = Field(default=0, ge=0)
    frequency: str = "occasional"
    onset: str = "gradual"
    notes: str = ""


class ScreeningRequest(BaseModel):
    patient_id: Optional[int] = None
    symptoms: List[SymptomInput] = []
    voice: Optional[dict] = None
    camera: Optional[dict] = None
    motion: Optional[dict] = None
    demo_mode: bool = False


class BenchmarkResult(BaseModel):
    model: str
    accuracy: float
    sensitivity: float
    specificity: float
    precision: float
    recall: float
    f1: float
    roc_auc: float
    training_time: float
    inference_time: float
    robustness: float
    generalization: float
