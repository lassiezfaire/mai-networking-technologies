# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы requirements.txt и устанавливаем зависимости
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы приложения
COPY . .

# Указываем, что контейнер должен прослушивать порт 5000
EXPOSE 5000

# Команда для запуска приложения
CMD ["python", "app/main.py"]
