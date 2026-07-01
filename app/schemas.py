from pydantic import BaseModel
from typing import Optional

class MusteriBase(BaseModel):
    isim: str
    sirket_adi: str
    email: str
    aktif_mi: Optional[bool] = True

class MusteriOlustur(MusteriBase):
    pass  # Veri eklerken ID'ye ihtiyacımız yok, otomatik artacak

class MusteriResponse(MusteriBase):
    id: int
    class Config:
        from_attributes = True  # SQLAlchemy nesnesini otomatik JSON'a çevirir