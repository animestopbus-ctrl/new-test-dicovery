FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y gcc && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY bot/. /app/

RUN useradd -m botuser && chown -R botuser /app
USER botuser

CMD ["python", "main.py"]
