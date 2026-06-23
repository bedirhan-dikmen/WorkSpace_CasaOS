from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class MusteriModel(Base):
    __tablename__ = "musteriler"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    isim = Column(String(100), nullable=False)
    sirket_adi = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True)
    aktif_mi = Column(Boolean, default=True)