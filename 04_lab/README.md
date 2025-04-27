# Kubernetes, часть 1
### Задание

Задания как такового не было, поэтому я просто сделал нечто работоспособное. 

### Результат
В Deployment работает образ на базе Ngnix.
### Как запустить
1. Запустить кластер `k3d cluster create dev-cluster --api-port <вставить-ip>:6443 --port 8443:443@loadbalancer  --port 8080:80@loadbalancer --volume $(pwd)/k3dvol:/tmp/k3dvol --servers 1 --agents 1`
2. Собрать образ локально: `docker build -t nginx-frontend:latest .`
3. Импортировать образ в кластер: `k3d image import nginx-frontend:latest -c dev-cluster`
4. Ввести команду `kubectl apply -f nginx-deployment.yaml`
5. Пробросить порты: `kubectl port-forward <имя-пода> <свободный-порт>:80`