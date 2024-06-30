# используем базовый образ Python версии 3
FROM python:3

# устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# копируем файл с зависимостями проекта в рабочую директорию внутри контейнера
COPY ./requirements.txt .

# устанавливаем зависимости внутри контейнера
RUN pip install --no-cache-dir -r requirements.txt

# копируем код приложения из текущей папки в рабочую директорию внутри контейнера
COPY . .