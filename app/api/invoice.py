from fastapi import APIRouter, UploadFile, File
import os
import uuid
from app.services.queue import push_job
from app.schemas.invoice import InvoiceResposne
from sqlalchemy.future import select

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
        
    async with AsyncSessionLocal() as session:
        invoice = Invoice(
            file_id=file_id,
            filename=file.filename,
            status="pending"
        )
        session.add(invoice)
        await session.commit()

    job = {
        "file_id": file_id,
        "path": file_path
    }

    push_job(job)

    return {
        "status": "queued",
        "file_id": file_id
    }
    # return {
    #     "file_id": file_id,
    #     "filename": file.filename,
    #     "path": file_path
    # }


@router.get("/{file_id}", response_model=InvoiceResponse)
async def get_invoice(file_id: str):
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Invoice).where(Invoice.file_id == file_id)
        )
        invoice = result.scaller_one_or_none()
        
        if not invoice:
            return {"error":"Invoice not found"}
        
        return invoice
    
@router.get("/", response_model=list[InvoiceResposne])
async def list_invoices(skip: int=0, limit: int = 10):
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Invoice).offset(skip).limit(limit)
        )
        invoices = result.scallers().all()
        
        return invoices