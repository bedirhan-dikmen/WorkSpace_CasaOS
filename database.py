import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# MySQL Bağlantı Adresi
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("HATA: .env dosyası bulunamadı veya DATABASE_URL tanımlanmadı!")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
# Modellerimizin türeyeceği ana sınıf
Base = declarative_base()

# Bağımlılık Enjeksiyonu (Dependency Injection) fonksiyonu
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()