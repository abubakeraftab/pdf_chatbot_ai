FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
 build-essential \
 poppler-utils \
 && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
ENV PYTHONBUFFERED=1

CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]
