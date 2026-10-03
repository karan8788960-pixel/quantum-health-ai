from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import auth, screening, benchmark, reports, ml, patients, audit, datasets
from app.core.config import settings

app = FastAPI(
    title="Quantum Health AI",
    description="Multimodal AI + Hybrid Quantum Machine Learning for Early Health-Risk Screening",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.backend_cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for router in [auth.router, screening.router, benchmark.router, reports.router, ml.router, patients.router, audit.router, datasets.router]:
    app.include_router(router)

@app.get("/")
async def root():
    return {
        "name": "Quantum Health AI",
        "tagline": "Multimodal AI + Hybrid Quantum Machine Learning for Early Health-Risk Screening",
        "status": "operational",
        "safety_message": "This is a research/decision-support prototype and not a medical diagnosis."
    }

@app.get("/health")
async def health():
    return {"status": "ok"}
