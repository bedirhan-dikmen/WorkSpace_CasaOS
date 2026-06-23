from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# 1. FastAPI Uygulamasını Başlatıyoruz
app = FastAPI(title="Yebsoft Müşteri Otomasyonu API")

# 2. JSON Veri Modelimizi Tanımlıyoruz
class Musteri(BaseModel):
    id: int
    isim: str
    sirket_adi: str
    email: str
    aktif_mi: Optional[bool] = True

# 3. Geçici Veri Tabanımız (RAM üzerinde)
db: List[Musteri] = [
    Musteri(id=1, isim="Ahmet Yılmaz", sirket_adi="Yebsoft", email="ahmet@yebsoft.net", aktif_mi=True),
    Musteri(id=2, isim="bedi", sirket_adi="Yebsoft", email="bedi@yebsoft.net", aktif_mi=True)
]

@app.get("/")
def ana_sayfa():
    return {"mesaj": "Yebsoft Müşteri Otomasyonu API'sine Hoş Geldiniz!"}


# --- CRUD İŞLEMLERİ ---

# READ (Listeleme)
@app.get("/musteriler", response_model=List[Musteri])
def tum_musterileri_getir():
    return db

# READ (Detay)
@app.get("/musteriler/{musteri_id}", response_model=Musteri)
def musteri_getir(musteri_id: int):
    for m in db:
        if m.id == musteri_id:
            return m
    raise HTTPException(status_code=404, detail="Müşteri bulunamadı!")

# CREATE (Ekleme)
@app.post("/musteriler", response_model=Musteri)
def yeni_musteri_ekle(yeni_musteri: Musteri):
    for m in db:
        if m.id == yeni_musteri.id:
            raise HTTPException(status_code=400, detail="Bu ID zaten kullanımda.")
    db.append(yeni_musteri)
    return yeni_musteri

# UPDATE (Güncelleme)
@app.put("/musteriler/{musteri_id}", response_model=Musteri)
def musteri_guncelle(musteri_id: int, guncel_bilgiler: Musteri):
    for index, m in enumerate(db):
        if m.id == musteri_id:
            db[index] = guncel_bilgiler
            return guncel_bilgiler
    raise HTTPException(status_code=404, detail="Güncellenecek müşteri bulunamadı!")

# DELETE (Silme)
@app.delete("/musteriler/{musteri_id}")
def musteri_sil(musteri_id: int):
    for index, m in enumerate(db):
        if m.id == musteri_id:
            db.pop(index)
            return {"mesaj": f"ID'si {musteri_id} olan müşteri başarıyla silindi."}
    raise HTTPException(status_code=404, detail="Silinecek müşteri bulunamadı!")