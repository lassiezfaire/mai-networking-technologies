# Первый этап: используем официальный образ Python для установки зависимостей
FROM python:3.9-slim AS builder

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

FROM scratch

COPY --from=builder /usr/local/bin/python3.9 /usr/local/bin/python
COPY --from=builder /usr/local/lib/libpython3.9.so.1.0 /usr/local/lib/libpython3.9.so.1.0
COPY --from=builder /usr/local/lib/python3.9 /usr/local/lib/python3.9
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /lib/x86_64-linux-gnu/libc.so.6 /lib/x86_64-linux-gnu/libc.so.6
COPY --from=builder /lib/x86_64-linux-gnu/libm.so.6 /lib/x86_64-linux-gnu/libm.so.6
COPY --from=builder /lib/x86_64-linux-gnu/libz.so.1 /lib/x86_64-linux-gnu/libz.so.1
COPY --from=builder /lib64/ld-linux-x86-64.so.2 /lib64/ld-linux-x86-64.so.2
COPY --from=builder /app /app

WORKDIR /app

EXPOSE 5000

CMD ["/usr/local/bin/python", "app/main.py"]
