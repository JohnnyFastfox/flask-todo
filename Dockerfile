FROM python:3.10-slim
WORKDIR /app

# requirements.txt mit psycopg2-binary kopieren und abhängen
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
ENV PYTHONUNBUFFERED=1
CMD ["python", "flask-todo.py"]
