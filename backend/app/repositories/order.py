from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.models.order import Order
from app.repositories.base import BaseRepository


class OrderRepository(BaseRepository[Order]):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(Order, db)

    async def get_user_orders(self, user_id: int, skip: int = 0, limit: int = 20) -> list[Order]:
        result = await self.db.execute(
            select(Order)
            .where(Order.user_id == user_id)
            .options(joinedload(Order.items), joinedload(Order.user))
            .order_by(Order.created_at.desc())
            .offset(skip)
            .limit(limit)
        )
        return list(result.unique().scalars().all())

    async def get_all_orders(self, skip: int = 0, limit: int = 50) -> list[Order]:
        result = await self.db.execute(
            select(Order)
            .options(joinedload(Order.items), joinedload(Order.user))
            .order_by(Order.created_at.desc())
            .offset(skip)
            .limit(limit)
        )
        return list(result.unique().scalars().all())

    async def get_order_with_items(self, order_id: int) -> Optional[Order]:
        result = await self.db.execute(
            select(Order)
            .where(Order.id == order_id)
            .options(joinedload(Order.items), joinedload(Order.user))
        )
        return result.unique().scalar_one_or_none()
