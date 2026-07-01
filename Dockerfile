# 1. Resmi hafif Python imajını taban alıyoruz [cite: 9]
FROM python:3.10-slim

# 2. Konteyner içinde çalışma dizini oluşturuyoruz
WORKDIR /app

# 3. Önce sistem bağımlılıklarını yüklüyoruz (MySQL kütüphaneleri için şart) 
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# 4. Bağımlılık listesini kopyalayıp yüklüyoruz 
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt 

# 5. Projenin kalan tüm dosyalarını konteyner içine kopyalıyoruz
COPY . .

# 6. Uygulamayı ayağa kaldıran ana komut (.py uzantısı kaldırıldı ve iç port 8000 yapıldı) 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]