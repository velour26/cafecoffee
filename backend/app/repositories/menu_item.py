from decimal import Decimal
from typing import Optional

from sqlalchemy import and_, func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.models.menu_item import MenuItem
from app.repositories.base import BaseRepository


class MenuItemRepository(BaseRepository[MenuItem]):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(MenuItem, db)

    async def get_with_category(self, item_id: int) -> Optional[MenuItem]:
        result = await self.db.execute(
            select(MenuItem)
            .where(MenuItem.id == item_id)
            .options(joinedload(MenuItem.category))
        )
        return result.scalar_one_or_none()

    async def get_filtered(
        self,
        category_id: Optional[int] = None,
        search: Optional[str] = None,
        min_price: Optional[Decimal] = None,
        max_price: Optional[Decimal] = None,
        skip: int = 0,
        limit: int = 20,
        only_active: bool = True,
    ) -> list[MenuItem]:
        query = select(MenuItem).options(joinedload(MenuItem.category))
        conditions = []
        if only_active:
            conditions.append(MenuItem.is_active == True)
        if category_id is not None:
            conditions.append(MenuItem.category_id == category_id)
        if search:
            conditions.append(MenuItem.name.ilike(f"%{search}%"))
        if min_price is not None:
            conditions.append(MenuItem.price >= min_price)
        if max_price is not None:
            conditions.append(MenuItem.price <= max_price)
        if conditions:
            query = query.where(and_(*conditions))
        query = query.order_by(MenuItem.name).offset(skip).limit(limit)
        result = await self.db.execute(query)
        return list(result.scalars().all())

    async def count_filtered(
        self,
        category_id: Optional[int] = None,
        search: Optional[str] = None,
        min_price: Optional[Decimal] = None,
        max_price: Optional[Decimal] = None,
        only_active: bool = True,
    ) -> int:
        query = select(func.count(MenuItem.id))
        conditions = []
        if only_active:
            conditions.append(MenuItem.is_active == True)
        if category_id is not None:
            conditions.append(MenuItem.category_id == category_id)
        if search:
            conditions.append(MenuItem.name.ilike(f"%{search}%"))
        if min_price is not None:
            conditions.append(MenuItem.price >= min_price)
        if max_price is not None:
            conditions.append(MenuItem.price <= max_price)
        if conditions:
            query = query.where(and_(*conditions))
        result = await self.db.execute(query)
        return result.scalar_one()
