# Кофеёчек ☕

Веб-приложение для кофейни. FastAPI + PostgreSQL на бэкенде, Vue 3 + Tailwind CSS на фронтенде.

## Быстрый старт (Docker)

```bash
cp .env.example .env
docker compose up --build
```

- Фронтенд: http://localhost
- API: http://localhost:8000/api/v1
- Документация API: http://localhost:8000/docs

**Учётная запись администратора:**
- Email: `admin@coffeecheck.ru`
- Пароль: `admin12345`

## Локальная разработка

### Бэкенд

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Запустить PostgreSQL (например через Docker)
docker run -d --name cafe-db \
  -e POSTGRES_DB=cafe_db \
  -e POSTGRES_USER=cafe_user \
  -e POSTGRES_PASSWORD=cafe_pass \
  -p 5432:5432 postgres:16-alpine

# Создать файл .env
cp ../.env.example .env

# Применить миграции и загрузить данные
alembic upgrade head
python seed.py

# Запустить сервер
uvicorn app.main:app --reload
```

### Фронтенд

```bash
cd frontend
npm install
cp ../.env.example .env.local  # отредактировать VITE_API_URL при необходимости
npm run dev
```

## Стек

| Слой | Технологии |
|------|-----------|
| Backend | FastAPI, SQLAlchemy 2.0 (async), asyncpg, Alembic, Pydantic v2, passlib, python-jose |
| Frontend | Vue 3, Vite, Pinia, Vue Router 4, Axios, Tailwind CSS |
| База данных | PostgreSQL 16 |
| Деплой | Docker, Docker Compose, Nginx |

## Функциональность

**Покупатель:**
- Просмотр меню с фильтрами по категории и цене
- Страница детального просмотра позиции
- Корзина и оформление заказа
- История заказов
- Отзывы на позиции меню (только при наличии заказа)
- Избранное
- Профиль с редактированием данных

**Администратор:**
- Дашборд со статистикой
- CRUD категорий
- CRUD позиций меню (мягкое удаление)
- Управление статусами заказов
