import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# .env dosyasını yüklüyoruz (Yerel geliştirme için)
load_dotenv()

# CasaOS/Docker ortam değişkenlerinden parçalı olarak verileri çekiyoruz
# Eğer bu değişkenler sistemde yoksa, sağ taraftaki varsayılan değerleri kullanır
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "Sifreniz123*")  # Kendi yerel şifreni yazabilirsin
DB_NAME = os.getenv("DB_NAME", "workspace_db")          # Kendi local db adını yazabilirsin

# SQLALCHMEY DATABASE URL'ini dinamik ve güvenli bir şekilde inşa ediyoruz
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Eğer .env içinde doğrudan tam URL varsa onu da ezmemek için kontrol ekleyelim:
if os.getenv("DATABASE_URL"):
    SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Engine ve Session Yapılandırması
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Bağımlılık Enjeksiyonu (Dependency Injection) için db oturumu
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()