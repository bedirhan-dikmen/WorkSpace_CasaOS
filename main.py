from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

# Diğer dosyalardan ihtiyaç duyduğumuz yapıları çağırıyoruz
import models
import schemas
from database import engine, get_db

# Uygulama ayağa kalkarken MySQL tablolarını otomatik oluşturur
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Yebsoft Katmanlı Mimari API")

# --- CRUD İŞLEMLERİ ---

@app.get("/musteriler", response_model=List[schemas.MusteriResponse])
def tum_musterileri_getir(db: Session = Depends(get_db)):
    return db.query(models.MusteriModel).all()

@app.get("/musteriler/{musteri_id}", response_model=schemas.MusteriResponse)
def musteri_getir(musteri_id: int, db: Session = Depends(get_db)):
    musteri = db.query(models.MusteriModel).filter(models.MusteriModel.id == musteri_id).first()
    if not musteri:
        raise HTTPException(status_code=404, detail="Müşteri bulunamadı!")
    return musteri

@app.post("/musteriler", response_model=schemas.MusteriResponse)
def yeni_musteri_ekle(musteri_bilgisi: schemas.MusteriOlustur, db: Session = Depends(get_db)):
    email_kontrol = db.query(models.MusteriModel).filter(models.MusteriModel.email == musteri_bilgisi.email).first()
    if email_kontrol:
        raise HTTPException(status_code=400, detail="Bu email adresi zaten kayıtlı!")
        
    yeni_musteri = models.MusteriModel(**musteri_bilgisi.model_dump())
    db.add(yeni_musteri)
    db.commit()
    db.refresh(yeni_musteri)
    return yeni_musteri

@app.put("/musteriler/{musteri_id}", response_model=schemas.MusteriResponse)
def musteri_guncelle(musteri_id: int, guncel_bilgiler: schemas.MusteriOlustur, db: Session = Depends(get_db)):
    musteri = db.query(models.MusteriModel).filter(models.MusteriModel.id == musteri_id).first()
    if not musteri:
        raise HTTPException(status_code=404, detail="Güncellenecek müşteri bulunamadı!")
        
    for key, value in guncel_bilgiler.model_dump().items():
        setattr(musteri, key, value)
        
    db.commit()
    db.refresh(musteri)
    return musteri

@app.delete("/musteriler/{musteri_id}")
def musteri_sil(musteri_id: int, db: Session = Depends(get_db)):
    musteri = db.query(models.MusteriModel).filter(models.MusteriModel.id == musteri_id).first()
    if not musteri:
        raise HTTPException(status_code=404, detail="Silinecek müşteri bulunamadı!")
        
    db.delete(musteri)
    db.commit()
    return {"mesaj": f"ID'si {musteri_id} olan müşteri başarıyla silindi."}