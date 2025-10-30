from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    APP_NAME: str = "WhatBirdApp API"
    API_PREFIX: str = "/api"
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8080",
        "http://localhost:5173"
    ]
    PROJECT_ROOT: str = ".."
    ML_ROOT: str = "../ml"
    BIRDNET_ROOT: str = "../ml/birdnet-analyzer"

    class Config:
        env_file = ".env"

settings = Settings()
