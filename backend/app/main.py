import asyncio
import logging
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.v1.router import api_router
from app.core.config import settings

STATIC_DIR = Path(__file__).parent.parent / "static"
STATIC_DIR.mkdir(exist_ok=True)
(STATIC_DIR / "images").mkdir(exist_ok=True)

logger = logging.getLogger(__name__)


async def _run_seed():
    """Запускаем seed в фоне — не блокирует старт uvicorn."""
    try:
        # Импортируем здесь чтобы не тянуть при каждом запросе
        from seed import seed  # noqa: PLC0415
        await seed()
    except Exception as exc:
        logger.warning("Seed пропущен: %s", exc)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Запускаем seed в фоновой задаче — uvicorn уже принимает запросы
    asyncio.create_task(_run_seed())
    yield


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="REST API для кафе «Кофеёчек» — меню, заказы, корзина, отзывы",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
app.include_router(api_router, prefix="/api/v1")


@app.get("/health", tags=["Health"])
async def health_check():
    return {
        "status": "ok",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
    }
