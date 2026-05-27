FROM python:3.12-slim

WORKDIR /app

# Зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Исходники
COPY . .

# Папка для SQLite — Railway Volume монтируется сюда
RUN mkdir -p /data

# SQLite живёт в /data/cafe.db (Railway Volume → данные не пропадают при деплое)
ENV DATABASE_URL=sqlite+aiosqlite:////data/cafe.db

# Railway сам задаёт PORT
EXPOSE 8000

# 1. Применяем миграции (создают таблицы)
# 2. Заполняем тестовыми данными (seed.py пропускает если уже есть данные)
# 3. Запускаем сервер
CMD sh -c "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"
