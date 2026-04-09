from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import declarative_base
import datetime

Base = declarative_base()


class Invoice(Base):
    __table__ = "invoices"

    id = Column(Integer, primary_key=True)
    file_id = Column(String)
    filename = Column(String)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
