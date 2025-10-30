import sys
import os
import shutil
import uuid
from fastapi import UploadFile

# Add project root (whatbirdapp/) so ml/ becomes importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from ml.infer import identify_bird  # now works ✅

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'uploads')
os.makedirs(UPLOAD_DIR, exist_ok=True)

async def run_inference_on_file(file: UploadFile):
    """
    Save uploaded audio file temporarily, run ML inference, then delete it.
    """
    file_ext = os.path.splitext(file.filename)[1]
    temp_filename = f"{uuid.uuid4()}{file_ext}"
    temp_path = os.path.join(UPLOAD_DIR, temp_filename)

    # Save file
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        result = identify_bird(temp_path)
    except Exception as e:
        result = {"error": str(e)}
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

    return result

