# backend/app/schemas/predict.py
from typing import List
from pydantic import BaseModel

class Detection(BaseModel):
    common_name: str
    confidence: float

class PredictResponse(BaseModel):
    predictions: List[Detection]
