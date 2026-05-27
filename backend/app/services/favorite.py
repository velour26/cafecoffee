from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.favorite import Favorite
from app.repositories.favorite import FavoriteRepository
from app.repositories.menu_item import MenuItemRepository


class FavoriteService:
    def __init__(self, db: AsyncSession) -> None:
        self.fav_repo = FavoriteRepository(db)
        self.menu_repo = MenuItemRepository(db)

    async def get_favorites(self, user_id: int) -> list[Favorite]:
        return await self.fav_repo.get_user_favorites(user_id)

    async def add_favorite(self, user_id: int, menu_item_id: int) -> Favorite:
        menu_item = await self.menu_repo.get_by_id(menu_item_id)
        if not menu_item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Позиция меню не найдена"
            )
        existing = await self.fav_repo.get_user_favorite(user_id, menu_item_id)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Уже в избранном"
            )
        fav = Favorite(user_id=user_id, menu_item_id=menu_item_id)
        return await self.fav_repo.create(fav)

    async def remove_favorite(self, user_id: int, menu_item_id: int) -> None:
        fav = await self.fav_repo.get_user_favorite(user_id, menu_item_id)
        if not fav:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Позиция не найдена в избранном",
            )
        await self.fav_repo.delete(fav)
