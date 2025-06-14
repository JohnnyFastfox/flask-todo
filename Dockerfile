FROM python:3.13.4-slim
WORKDIR /app

# requirements.txt mit psycopg2-binary kopieren und abhängen
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

ENTRYPOINT ["/app/entrypoint.sh"]
