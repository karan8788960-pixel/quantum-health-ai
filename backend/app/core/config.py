from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    app_name: str = "Quantum Health AI"
    env: str = "development"
    debug: bool = True
    secret_key: str = "dev-secret-key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 120
    backend_cors_origins: List[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]
    database_url: str = "sqlite:///./quantum_health_ai.db"

    class Config:
        env_file = ".env"


settings = Settings()
