# backend/app/routes/identify.py
import os
import shutil
import tempfile
from datetime import datetime
from fastapi import APIRouter, UploadFile, File, HTTPException, Query
from fastapi.responses import JSONResponse

from ..core.config import settings
from ..schemas.predict import PredictResponse, Detection
from ..services.bird_service import predict_from_file

router = APIRouter(prefix="", tags=["identify"])

@router.post("/identify", response_model=PredictResponse)
async def identify(
    file: UploadFile = File(..., description="Audio file (wav/mp3/m4a/etc.)"),
    lat: float = Query(..., description="Latitude"),
    lon: float = Query(..., description="Longitude"),
    min_confidence: float = Query(0.1, ge=0.0, le=1.0),
    top_k: int = Query(3, ge=1, le=50, description="Return top N predictions (default 3)"),
    date: str | None = Query(None, description="ISO date-time (optional)"),
):
    # Size guardrail (if client supplies size)
    content_length = file.size if hasattr(file, "size") else None
    if content_length and content_length > settings.max_file_size_mb * 1024 * 1024:
        raise HTTPException(status_code=413, detail="File too large")

    # Persist upload to temp file
    suffix = os.path.splitext(file.filename or "")[1].lower()
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix or ".wav")
    try:
        with tmp as out:
            shutil.copyfileobj(file.file, out)

        # Parse date if provided
        when = None
        if date:
            try:
                when = datetime.fromisoformat(date)
            except Exception as e:
                raise HTTPException(status_code=400, detail=f"Invalid date: {e}")

        preds = predict_from_file(
            file_path=tmp.name, lat=lat, lon=lon, when=when, min_confidence=min_confidence
        )

        # Apply top_k limit
        preds = preds[:top_k]

        formatted = []
        for p in preds:
            formatted.append({
                "common_name": p["common_name"],
                "confidence": p["confidence"],
                "confidence_percent": f"{p['confidence'] * 100:.2f}%"  # format
            })

        return PredictResponse(predictions=[Detection(**f) for f in formatted])

    finally:
        try:
            if os.path.exists(tmp.name):
                os.remove(tmp.name)
        except Exception:
            pass
