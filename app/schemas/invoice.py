from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime

class InvoiceResposne(BaseModel):
    file_id: str
    filename: str
    status: str
    extracted_data: Optional[Dict] = None
    error: Optional[str] = None
    retry_count: int
    created_at: datetime
    
    class Config:
        from_attributes = True