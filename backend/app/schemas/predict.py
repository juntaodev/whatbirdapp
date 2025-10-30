from pydantic import BaseModel
from typing import List, Optional

class Prediction(BaseModel):
    scientific_name: str
    common_name: str
    confidence: float
    start_s: float
    end_s: float

class IdentifyResponse(BaseModel):
    ok: bool
    count: int
    predictions: List[Prediction]
    spectrogram_url: Optional[str] = None
    processing_ms: int
