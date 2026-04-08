from fastapi import FastAPI
from app.api.invoice import router as invoice_router

app = FastAPI(title="AI Invoice Processor")

app.include_router(invoice_router, prefix="/invoice")


@app.get("/")
async def root():
    return {"message": "API is running"}
