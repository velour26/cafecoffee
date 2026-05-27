from typing import Optional

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.models.cart_item import CartItem
from app.models.menu_item import MenuItem
from app.repositories.base import BaseRepository


class CartRepository(BaseRepository[CartItem]):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(CartItem, db)

    async def get_user_cart(self, user_id: int) -> list[CartItem]:
        result = await self.db.execute(
            select(CartItem)
            .where(CartItem.user_id == user_id)
            .options(joinedload(CartItem.menu_item).joinedload(MenuItem.category))
            .order_by(CartItem.created_at)
        )
        return list(result.scalars().all())

    async def get_user_cart_item(self, user_id: int, cart_item_id: int) -> Optional[CartItem]:
        result = await self.db.execute(
            select(CartItem).where(
                CartItem.user_id == user_id, CartItem.id == cart_item_id
            )
        )
        return result.scalar_one_or_none()

    async def get_existing_item(self, user_id: int, menu_item_id: int) -> Optional[CartItem]:
        result = await self.db.execute(
            select(CartItem).where(
                CartItem.user_id == user_id, CartItem.menu_item_id == menu_item_id
            )
        )
        return result.scalar_one_or_none()

    async def clear_user_cart(self, user_id: int) -> None:
        await self.db.execute(delete(CartItem).where(CartItem.user_id == user_id))
        await self.db.flush()
