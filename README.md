# Quantum Health AI

A multimodal, explainable, research-focused early screening prototype for SIH 2026 Problem Statement 26139.

## Overview

Quantum Health AI combines symptom reporting, voice features, camera-based motion capture, and motion-sensor telemetry into a hybrid classical + quantum screening pipeline. It is designed for early-risk screening and clinical decision support, not autonomous diagnosis.

## SIH26139 Mapping

- Multimodal AI + hybrid quantum ML: implemented through a modular preprocessing and fusion pipeline
- Explainability + uncertainty: included in reporting and reliability engine
- Benchmarking and model comparison: classical vs quantum vs hybrid comparison
- Research workflow: experiment tracking, dataset versioning, report generation
- Safety-first design: explicit guardrails and no medical diagnosis language

## Architecture

- Frontend: React + TypeScript + Vite + Tailwind CSS
- Backend: FastAPI + Pydantic + SQLAlchemy + SQLite fallback
- ML: scikit-learn pipelines for classical models
- QML: Qiskit circuit-based simulation
- Security: JWT-based role-aware auth and audit logging

## Features

- Landing page and research-lab themed dashboard
- Role-based access for doctor, researcher, admin, and patient
- Guided patient screening workflow
- Voice, camera, and motion sensor capture interfaces with fallbacks
- Multimodal feature fusion
- Classical ML, quantum ML, hybrid QML pipelines
- Explainability and reliability output
- Benchmark comparison and experiment history
- PDF report generation and audit trail

## Setup

### Frontend

```bash
cd frontend
npm install
npm run dev -- --host 0.0.0.0
```

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Database

The default configuration uses SQLite for local development. The database file is created automatically when the backend starts.

### Environment Variables

Copy `.env.example` to `.env` and update values as needed.

## Demo

1. Start backend.
2. Start frontend.
3. Go to the landing page.
4. Choose `Start Screening` or `Start Demo`.
5. Complete the wizard and analyze results.

## API Documentation

Once the backend is running, open:

- http://localhost:8000/docs
- http://localhost:8000/redoc

## Testing

Frontend:

```bash
cd frontend
npm test -- --run
```

Backend:

```bash
cd backend
pytest
```

## Limitations

- This is a research prototype and not a clinical diagnosis system.
- Real hardware execution is optional and not required for local demo execution.
- Sensor capture depends on browser permissions and device support.

## Future Scope

- Real hospital-grade multimodal datasets
- Production-grade patient consent workflows
- Real clinical validation and bias auditing
- Hardware backend integration with quantum providers
- Federated learning and privacy-preserving storage
