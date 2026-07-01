import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# .env dosyasını yüklüyoruz
load_dotenv()

# Tamamen senin istediğin isimlerle ortam değişkenlerini çekiyoruz
# Eğer .env okunamazsa, Docker bridge ağında hata vermemesi için mantıklı varsayılanlar atadık
DB_HOST = os.getenv("DB_HOST", "db")  # Docker ağındaki varsayılan servis adı
DB_PORT = os.getenv("DB_PORT", "3306")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "database_sifresi")
DB_NAME = os.getenv("DB_NAME", "database_adi")

# SQLALCHEMY DATABASE URL'ini dinamik olarak inşa ediyoruz 
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Engine ve Session Yapılandırması 
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Bağımlılık Enjeksiyonu için db oturumu 
def get_db(): 
    db = SessionLocal() 
    try: 
        yield db 
    finally:
        db.close()