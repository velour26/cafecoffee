# Кофеёчек (Cafe) — Архитектура

## Назначение
Веб-приложение кофейни: меню с категориями, корзина, оформление заказа с выбором доставки или самовывоза, отслеживание статуса заказа, отзывы (только после покупки) и админ-дашборд.

## Технологический стек

### Backend
- Python + **FastAPI 0.115**
- ORM: **SQLAlchemy 2.0 (async)** + `asyncpg`
- БД: **PostgreSQL 16-alpine**
- Авторизация: **JWT** (`python-jose`) + bcrypt (`passlib`)
- Миграции: **Alembic**, sed-скрипт `seed.py`
- Pydantic v2

### Frontend
- **Vue 3** (Composition API)
- Сборщик: **Vite 6**
- State: **Pinia 2**
- Роутер: **Vue Router 4** (вложенные маршруты + guards)
- HTTP: **Axios 1.7**
- UI: **Tailwind CSS 3.4**

### Инфраструктура (`docker-compose.yml`)
| Сервис | Образ | Порт | Особенности |
|---|---|---|---|
| `db` | `postgres:16-alpine` | внутренний | healthcheck `pg_isready` |
| `backend` | build `./backend` | 8000 | команда: `alembic upgrade head && python seed.py && uvicorn` |
| `frontend` | build `./frontend` (с Nginx) | **80** | build-arg `VITE_API_URL` |

> Есть отдельный `docker-compose.dev.yml` для локальной разработки.

## Структура каталогов
```
cafe/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── api/v1/
│   │   │   ├── router.py
│   │   │   └── endpoints/
│   │   │       ├── auth.py
│   │   │       ├── categories.py
│   │   │       ├── menu_items.py
│   │   │       ├── cart.py
│   │   │       ├── orders.py
│   │   │       ├── reviews.py
│   │   │       └── favorites.py
│   │   ├── core/         # config, security, dependencies
│   │   ├── db/           # base, session, seed
│   │   ├── models/       # 10 файлов
│   │   ├── schemas/
│   │   ├── services/
│   │   └── repositories/
│   ├── alembic/          # 2 миграции
│   ├── seed.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── api/          # axios модули
│   │   ├── stores/       # Pinia
│   │   ├── router/       # с guards
│   │   ├── layouts/      # Default, Dashboard, Admin
│   │   ├── views/        # 16 страниц + admin/
│   │   ├── components/
│   │   ├── utils/
│   │   └── main.js
│   └── Dockerfile (Nginx)
├── docker-compose.yml
├── docker-compose.dev.yml
└── README.md
```

## Модель данных
| Сущность | Назначение |
|---|---|
| `User` | Пользователь, привязка к `Role` |
| `Role` | admin / user |
| `Category` | Категория меню |
| `MenuItem` | Позиция меню (цена `Numeric`, вес в граммах, `is_active` — мягкое удаление) |
| `CartItem` | Позиция в корзине пользователя |
| `Order` + `OrderItem` | Заказ и его позиции, статусная машина (`OrderStatus` enum) |
| `Review` | Отзыв на позицию (только если у юзера есть выполненный заказ с этой позицией) |
| `Favorite` | Избранные позиции пользователя |

Статусы заказа: `new → confirmed → preparing → ready → completed / cancelled`.

## API
Префикс: `/api/v1`. Подключён через `app/api/v1/router.py`.

**Auth** (`auth.py`)
- `POST /auth/register`, `POST /auth/login`, `GET /auth/me`

**Categories** (`categories.py`)
- `GET /categories`, `POST/PUT/DELETE` *(admin)*

**Menu items** (`menu_items.py`)
- `GET /menu-items`, `GET /menu-items/{id}`, поиск
- `POST/PUT/DELETE` *(admin)* — мягкое удаление через `is_active`

**Cart** (`cart.py`)
- `GET /cart`, `POST /cart`, `PATCH /cart/{item_id}`, `DELETE /cart/{item_id}`

**Orders** (`orders.py`)
- `POST /orders` — оформить из корзины
- `GET /orders/my`, `GET /orders/{id}`
- `GET /orders` *(admin)*, `PATCH /orders/{id}/status` *(admin)*

**Reviews** (`reviews.py`)
- `GET /reviews`, `POST /reviews` *(требуется завершённый заказ с этой позицией)*

**Favorites** (`favorites.py`)
- `GET /favorites`, `POST /favorites`, `DELETE /favorites/{item_id}`

## Frontend: маршруты
Из `frontend/src/router/index.js`. Три layout-а: `DefaultLayout`, `DashboardLayout`, `AdminLayout`.

**Default (`/`)** — публичные:
- `/`, `/menu`, `/menu/:id`, `/categories`, `/reviews`, `/about`, `/contacts`, `/privacy`
- `/login`, `/register`
- `/cart`, `/order-success/:id` — `requiresAuth`

**Dashboard (`/account`)** — `requiresAuth`:
- `/account/profile`, `/account/orders`, `/account/orders/:id`

**Admin (`/admin`)** — `requiresAuth + requiresAdmin`:
- `/admin` (dashboard), `/admin/categories`, `/admin/menu`, `/admin/orders`, `/admin/reviews`

Catch-all `/:pathMatch(.*)*` → `/`.

## Ключевые фичи
- **Статусная машина заказа** с явными переходами и видимостью статусов в кабинете и админке.
- **«Отзыв только после покупки»** — серверная валидация по `OrderItem`.
- **Мягкое удаление** позиций меню (`is_active`) — заказы сохраняют ссылку.
- **Избранное** для зарегистрированных пользователей.
- **Доставка/самовывоз** как опция оформления.
- **Авто-миграции и сидинг** при старте контейнера backend.
- Frontend упакован в **Nginx**, build-arg `VITE_API_URL` зашивается на этапе сборки.

## Запуск
```bash
cp .env.example .env
docker compose up --build
```
- Frontend: <http://localhost>
- API: <http://localhost:8000/api/v1>
- Swagger: <http://localhost:8000/docs>
- Админ: `admin@coffeecheck.ru` / `admin12345`

## Замечания
- В проде фронт раздаётся **через Nginx**, а не Vite dev-server (в отличие от artistic/beauty-salon).
- Цены — `Numeric` (Decimal), не float.
- Ленивые импорты во всех роутах фронта (`() => import(...)`) — code-splitting по умолчанию.
- Для dev есть `docker-compose.dev.yml` (отдельная конфигурация).
