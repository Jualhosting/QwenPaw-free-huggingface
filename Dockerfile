FROM python:3.10-slim
RUN apt-get update && apt-get install -y libpq-dev gcc curl && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN printf "Yes\n" | qwenpaw init --defaults
CMD ["sh", "-c", "python3 sync.py download && (while true; do sleep 300; python3 sync.py upload; done &) && qwenpaw app --host 0.0.0.0 --port 7860"]
