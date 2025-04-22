# Используем официальный образ Nginx для обслуживания статических файлов
FROM nginx:alpine

# Копируем статический HTML-файл
COPY index.html /usr/share/nginx/html/index.html

# Копируем конфигурацию Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf
