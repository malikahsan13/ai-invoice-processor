from fastapi import APIRouter, UploadFile, File
import os
import uuid
from app.services.queue import push_job

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload-invoice")
async def upload_invoice(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    file_path = f"{UPLOAD_DIR}/{file_id}/{file.filename}"

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    job = {
        "file_id": file_id,
        "path": file_path
    }

    push_job(job)

    return {
        "file_id": file_id,
        "filename": file.filename,
        "path": file_path
    }
