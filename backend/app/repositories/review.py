from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.models.review import Review
from app.repositories.base import BaseRepository


class ReviewRepository(BaseRepository[Review]):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(Review, db)

    async def get_by_menu_item(self, menu_item_id: int) -> list[Review]:
        result = await self.db.execute(
            select(Review)
            .where(Review.menu_item_id == menu_item_id)
            .options(joinedload(Review.user))
            .order_by(Review.created_at.desc())
        )
        return list(result.scalars().all())

    async def get_all_reviews(self, skip: int = 0, limit: int = 50) -> list[Review]:
        result = await self.db.execute(
            select(Review)
            .options(joinedload(Review.user), joinedload(Review.menu_item))
            .order_by(Review.created_at.desc())
            .offset(skip)
            .limit(limit)
        )
        return list(result.scalars().all())

    async def get_user_review_for_item(self, user_id: int, menu_item_id: int) -> Optional[Review]:
        result = await self.db.execute(
            select(Review).where(
                Review.user_id == user_id, Review.menu_item_id == menu_item_id
            )
        )
        return result.scalar_one_or_none()
