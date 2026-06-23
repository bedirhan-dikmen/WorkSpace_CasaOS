from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# MySQL Bağlantı Adresi
DATABASE_URL = "mysql+pymysql://root:Republic.8495@localhost:3306/yebsoft_db"

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