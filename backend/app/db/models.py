from sqlalchemy import Column, Integer, String, Text, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base


class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True, nullable=False)
    description = Column(Text, default="")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    full_name = Column(String(255), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    role = relationship("Role")


class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=True)
    sex = Column(String(20), nullable=True)
    medical_history = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)


class Screening(Base):
    __tablename__ = "screenings"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=True)
    status = Column(String(50), default="draft")
    risk_level = Column(String(50), default="not_assessed")
    reliability = Column(String(50), default="unknown")
    data_quality = Column(String(50), default="unknown")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Symptom(Base):
    __tablename__ = "symptoms"
    id = Column(Integer, primary_key=True, index=True)
    screening_id = Column(Integer, ForeignKey("screenings.id"), nullable=False)
    name = Column(String(150), nullable=False)
    severity = Column(Integer, default=0)
    duration_days = Column(Integer, default=0)
    frequency = Column(String(50), default="occasional")
    onset = Column(String(50), default="gradual")
    notes = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)


class VoiceAssessment(Base):
    __tablename__ = "voice_assessments"
    id = Column(Integer, primary_key=True, index=True)
    screening_id = Column(Integer, ForeignKey("screenings.id"), nullable=False)
    permission_state = Column(String(50), default="ready")
    status = Column(String(50), default="ready")
    pitch_mean = Column(Float, default=0.0)
    amplitude_mean = Column(Float, default=0.0)
    speech_rate = Column(Float, default=0.0)
    pause_ratio = Column(Float, default=0.0)
    jitter = Column(Float, default=0.0)
    shimmer = Column(Float, default=0.0)
    signal_quality = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)


class CameraAssessment(Base):
    __tablename__ = "camera_assessments"
    id = Column(Integer, primary_key=True, index=True)
    screening_id = Column(Integer, ForeignKey("screenings.id"), nullable=False)
    status = Column(String(50), default="ready")
    signal_quality = Column(Float, default=0.0)
    amplitude = Column(Float, default=0.0)
    velocity = Column(Float, default=0.0)
    acceleration = Column(Float, default=0.0)
    frequency = Column(Float, default=0.0)
    smoothness = Column(Float, default=0.0)
    trajectory_variation = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)


class MotionAssessment(Base):
    __tablename__ = "motion_assessments"
    id = Column(Integer, primary_key=True, index=True)
    screening_id = Column(Integer, ForeignKey("screenings.id"), nullable=False)
    sensor_availability = Column(String(50), default="unavailable")
    acc_x = Column(Float, default=0.0)
    acc_y = Column(Float, default=0.0)
    acc_z = Column(Float, default=0.0)
    gyro_x = Column(Float, default=0.0)
    gyro_y = Column(Float, default=0.0)
    gyro_z = Column(Float, default=0.0)
    rms = Column(Float, default=0.0)
    variance = Column(Float, default=0.0)
    dominant_frequency = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)


class Dataset(Base):
    __tablename__ = "datasets"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    description = Column(Text, default="")
    source = Column(String(200), default="research")
    created_at = Column(DateTime, default=datetime.utcnow)


class DatasetVersion(Base):
    __tablename__ = "dataset_versions"
    id = Column(Integer, primary_key=True, index=True)
    dataset_id = Column(Integer, ForeignKey("datasets.id"), nullable=False)
    version = Column(String(100), nullable=False)
    notes = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)


class Experiment(Base):
    __tablename__ = "experiments"
    id = Column(Integer, primary_key=True, index=True)
    experiment_id = Column(String(100), unique=True, nullable=False)
    dataset_version = Column(String(100), default="v1")
    model_name = Column(String(100), default="")
    preprocessing = Column(Text, default="")
    features = Column(Text, default="")
    pca_settings = Column(Text, default="")
    qml_settings = Column(Text, default="")
    hyperparameters = Column(Text, default="")
    random_seed = Column(Integer, default=42)
    train_test_split = Column(String(100), default="80:20")
    metrics = Column(Text, default="")
    timestamp = Column(DateTime, default=datetime.utcnow)
    software_version = Column(String(100), default="0.1.0")


class Model(Base):
    __tablename__ = "models"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), unique=True, nullable=False)
    type = Column(String(50), default="classical")
    version = Column(String(50), default="v1")
    description = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)


class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True, index=True)
    screening_id = Column(Integer, ForeignKey("screenings.id"), nullable=False)
    model_name = Column(String(100), nullable=False)
    risk_label = Column(String(100), default="unknown")
    probability = Column(Float, default=0.0)
    reliability = Column(String(50), default="unknown")
    created_at = Column(DateTime, default=datetime.utcnow)


class Benchmark(Base):
    __tablename__ = "benchmarks"
    id = Column(Integer, primary_key=True, index=True)
    experiment_id = Column(String(100), nullable=False)
    model_name = Column(String(100), nullable=False)
    accuracy = Column(Float, default=0.0)
    sensitivity = Column(Float, default=0.0)
    specificity = Column(Float, default=0.0)
    precision = Column(Float, default=0.0)
    recall = Column(Float, default=0.0)
    f1 = Column(Float, default=0.0)
    roc_auc = Column(Float, default=0.0)
    training_time = Column(Float, default=0.0)
    inference_time = Column(Float, default=0.0)
    robustness = Column(Float, default=0.0)
    generalization = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)


class Report(Base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True, index=True)
    screening_id = Column(Integer, ForeignKey("screenings.id"), nullable=False)
    title = Column(String(200), default="Screening Report")
    status = Column(String(50), default="draft")
    generated_at = Column(DateTime, default=datetime.utcnow)


class AuditEvent(Base):
    __tablename__ = "audit_events"
    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String(100), nullable=False)
    actor = Column(String(100), default="system")
    metadata = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)


class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    doctor_name = Column(String(200), default="")
    appointment_time = Column(DateTime, default=datetime.utcnow)
    status = Column(String(50), default="scheduled")
    notes = Column(Text, default="")
