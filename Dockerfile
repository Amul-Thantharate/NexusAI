FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-dev \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 8501

HEALTHCHECK cmd curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT [ "streamlit", "run", "main.py", "--server.port", "8501", "--server.address", "0.0.0.0" ]
