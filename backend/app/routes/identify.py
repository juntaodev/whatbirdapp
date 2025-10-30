from fastapi import APIRouter, UploadFile
from app.services.bird_service import run_inference_on_file

router = APIRouter(prefix="/identify", tags=["Bird Identification"])

@router.post("/")
async def identify_bird_route(file: UploadFile):
    return await run_inference_on_file(file)
