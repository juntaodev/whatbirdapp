# backend/app/core/config.py
from pydantic import BaseModel
from typing import List

class Settings(BaseModel):
    allowed_extensions: List[str] = [".wav", ".mp3", ".m4a", ".flac", ".ogg", ".aac"]
    max_file_size_mb: int = 50  # basic guardrail

settings = Settings()
