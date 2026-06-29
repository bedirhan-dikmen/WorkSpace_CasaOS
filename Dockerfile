# 1. Resmi hafif Python imajını taban alıyoruz
FROM python:3.10-slim

# 2. Konteyner içinde çalışma dizini oluşturuyoruz
WORKDIR /app

# 3. Bağımlılıkları kopyalayıp yüklüyoruz
# (Eğer requirements.txt dosyan yoksa birazdan oluşturacağız)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Projenin kalan tüm dosyalarını konteyner içine kopyalıyoruz
COPY . .

# 5. Projenin çalışacağı portu belirtiyoruz (FastAPI için varsayılan 8000)
EXPOSE 8000

# 6. Uygulamayı ayağa kaldıran ana komut
CMD ["uvicorn", "main.py:app", "--host", "0.0.0.0", "--port", "8000"]