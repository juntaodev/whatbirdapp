# backend/app/services/bird_service.py
from __future__ import annotations
import os
import tempfile
from datetime import datetime
from typing import List, Dict, Any, Optional

from pydub import AudioSegment  # requires ffmpeg in PATH for non-wav
from birdnetlib.analyzer import Analyzer
from birdnetlib import Recording

# --- Analyzer singleton to avoid loading model for every request ---
_ANALYZER: Optional[Analyzer] = None

def _get_analyzer() -> Analyzer:
    global _ANALYZER
    if _ANALYZER is None:
        # Loads the model once; subsequent calls reuse it
        _ANALYZER = Analyzer()
    return _ANALYZER

# --- Helpers ---

def _ensure_wav(input_path: str) -> str:
    """
    Ensures we have a WAV file on disk.
    - If already .wav -> return as-is.
    - Else try to convert using pydub+ffmpeg.
    """
    ext = os.path.splitext(input_path)[1].lower()
    if ext == ".wav":
        return input_path

    # Convert to wav with pydub (requires ffmpeg available)
    audio = AudioSegment.from_file(input_path)  # ffmpeg handles most types
    tmp_wav = tempfile.NamedTemporaryFile(delete=False, suffix=".wav").name
    audio.export(tmp_wav, format="wav")
    return tmp_wav

def _preprocess(recording: Recording) -> None:
    """Light preprocessing to improve detection on varied files."""
    try:
        recording.convert_to_mono()
        recording.normalize()
    except Exception:
        # Preprocess is best-effort; don’t fail the whole request
        pass

# --- Public API ---

def predict_from_file(
    file_path: str,
    lat: float,
    lon: float,
    when: Optional[datetime] = None,
    min_confidence: float = 0.1,
) -> List[Dict[str, Any]]:
    """
    Runs BirdNET on the provided audio file (any common format if ffmpeg present).
    Returns a list of {common_name, confidence} sorted by confidence desc,
    filtered by min_confidence.
    """
    analyzer = _get_analyzer()
    when = when or datetime.now()

    # Ensure wav on disk (mp3/m4a will be converted if ffmpeg is available)
    wav_path = _ensure_wav(file_path)

    # Build recording
    rec = Recording(
        analyzer,
        wav_path,
        lat=lat,
        lon=lon,
        date=when,
    )

    _preprocess(rec)
    rec.analyze()  # (older birdnetlib: no min_confidence arg here)

    detections = rec.detections or []
    results = [
        {"common_name": d["common_name"], "confidence": float(d["confidence"])}
        for d in detections
        if float(d["confidence"]) >= float(min_confidence)
    ]

    # Sort by confidence desc
    results.sort(key=lambda r: r["confidence"], reverse=True)

    # Clean temp wav if we converted
    try:
        if wav_path != file_path and os.path.exists(wav_path):
            os.remove(wav_path)
    except Exception:
        pass

    return results
