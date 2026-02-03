FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY bot/. /app/

RUN useradd -m botuser && chown -R botuser /app
USER botuser

CMD ["python", "main.py"]
