FROM python:3.9-alpine AS builder

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.9-alpine

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /usr/local/bin/python /usr/local/bin/python

COPY . .

EXPOSE 5000

CMD ["python", "app/main.py"]
