"""AI-бариста: подбирает позицию из меню под настроение / погоду / запрос."""

from __future__ import annotations

import logging

from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession

from app import ai
from app.db.session import get_db
from app.repositories.menu_item import MenuItemRepository

logger = logging.getLogger(__name__)

router = APIRouter()

AI_FALLBACK_MESSAGE = (
    "🤖 AI-бариста сейчас прогревается — модель qwen2.5:3b загружается в память "
    "при первом запросе (это может занять до минуты). Попробуйте ещё раз через 30–60 секунд."
)


class AiAdvisorRequest(BaseModel):
    question: str = Field(min_length=3, max_length=500)


class AiAdvisorResponse(BaseModel):
    answer: str
    model: str


@router.post("/barista", response_model=AiAdvisorResponse)
async def ai_barista(
    payload: AiAdvisorRequest,
    db: AsyncSession = Depends(get_db),
) -> AiAdvisorResponse:
    repo = MenuItemRepository(db)
    items = await repo.get_filtered(skip=0, limit=40, only_active=True)

    lines: list[str] = []
    for item in items:
        cat = item.category.name if getattr(item, "category", None) else "—"
        weight = f", {item.weight_grams} г" if getattr(item, "weight_grams", None) else ""
        lines.append(f"- {item.name} ({cat}{weight}, {float(item.price):.0f} ₽)")
    menu_block = "\n".join(lines) if lines else "(меню пустое)"

    system = (
        "Ты — AI-бариста кофейни «Кофеёчек». "
        "Подбирай напиток или блюдо ТОЛЬКО из меню ниже, опираясь на настроение/погоду/запрос гостя. "
        "Отвечай коротко и тепло, на русском. Предлагай 1–3 позиции и объясняй почему. "
        "Не выдумывай позиций, которых нет в меню."
    )
    user = (
        f"Запрос гостя: {payload.question}\n\n"
        f"Меню кофейни:\n{menu_block}"
    )

    try:
        answer = await ai.chat(
            [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            max_tokens=500,
            temperature=0.7,
        )
    except Exception as exc:  # noqa: BLE001
        logger.warning("AI barista failed: %s", exc)
        return AiAdvisorResponse(answer=AI_FALLBACK_MESSAGE, model=ai.AI_MODEL)

    return AiAdvisorResponse(answer=answer, model=ai.AI_MODEL)
