from decimal import Decimal
from typing import Optional

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.menu_item import MenuItem
from app.repositories.menu_item import MenuItemRepository
from app.schemas.menu_item import MenuItemCreate, MenuItemUpdate


class MenuItemService:
    def __init__(self, db: AsyncSession) -> None:
        self.repo = MenuItemRepository(db)

    async def get_filtered(
        self,
        category_id: Optional[int] = None,
        search: Optional[str] = None,
        min_price: Optional[Decimal] = None,
        max_price: Optional[Decimal] = None,
        skip: int = 0,
        limit: int = 20,
        include_inactive: bool = False,
    ) -> dict:
        items = await self.repo.get_filtered(
            category_id=category_id,
            search=search,
            min_price=min_price,
            max_price=max_price,
            skip=skip,
            limit=limit,
            only_active=not include_inactive,
        )
        total = await self.repo.count_filtered(
            category_id=category_id,
            search=search,
            min_price=min_price,
            max_price=max_price,
            only_active=not include_inactive,
        )
        return {"items": items, "total": total, "skip": skip, "limit": limit}

    async def get_by_id(self, item_id: int) -> MenuItem:
        item = await self.repo.get_with_category(item_id)
        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Позиция меню не найдена"
            )
        return item

    async def create(self, data: MenuItemCreate) -> MenuItem:
        item = MenuItem(**data.model_dump())
        return await self.repo.create(item)

    async def update(self, item_id: int, data: MenuItemUpdate) -> MenuItem:
        item = await self.get_by_id(item_id)
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(item, field, value)
        await self.repo.db.flush()
        return item

    async def delete(self, item_id: int) -> None:
        item = await self.get_by_id(item_id)
        await self.repo.db.delete(item)
        await self.repo.db.flush()
