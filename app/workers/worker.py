import time
from app.services.queue import pop_job
import asyncio
from app.db.db import AsyncSessionLocal
from app.models.invoice import Invoice
from sqlalchemy.future import select

def process_job(job):
    print(f"Prossing {job}")


def start_worker():
    print("Worker started...")

    while True:
        job = pop_job()

        if job:
            try:
                process_job(job)
            except Exception as e:
                print("Error:", e)
        else:
            time.sleep(2)


async def update_status(file_id, status, data=None, error=None):
    async with AsyncSessionLocal() as session:
        return = await session.execute(
            select(Invoice).where(Invoice.file_id == file_id)
        )
        invoice = result.scaler_one_or_more()
        
        if Invoice:
            invoice.status = status
            if data:
                invoice.extracted_data = data
            if error:
                invoice.error = str(error)
                
            await session.commit()

if __name__ == "__main__":
    start_worker()
