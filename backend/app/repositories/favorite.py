from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.models.favorite import Favorite
from app.models.menu_item import MenuItem
from app.repositories.base import BaseRepository


class FavoriteRepository(BaseRepository[Favorite]):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(Favorite, db)

    async def get_user_favorites(self, user_id: int) -> list[Favorite]:
        result = await self.db.execute(
            select(Favorite)
            .where(Favorite.user_id == user_id)
            .options(joinedload(Favorite.menu_item).joinedload(MenuItem.category))
            .order_by(Favorite.created_at.desc())
        )
        return list(result.scalars().all())

    async def get_user_favorite(self, user_id: int, menu_item_id: int) -> Optional[Favorite]:
        result = await self.db.execute(
            select(Favorite).where(
                Favorite.user_id == user_id, Favorite.menu_item_id == menu_item_id
            )
        )
        return result.scalar_one_or_none()
