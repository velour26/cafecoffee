from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.category import Category
from app.repositories.category import CategoryRepository
from app.schemas.category import CategoryCreate, CategoryUpdate


class CategoryService:
    def __init__(self, db: AsyncSession) -> None:
        self.repo = CategoryRepository(db)

    async def get_all(self) -> list[Category]:
        return await self.repo.get_all(limit=200)

    async def get_by_id(self, category_id: int) -> Category:
        category = await self.repo.get_by_id(category_id)
        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Категория не найдена"
            )
        return category

    async def create(self, data: CategoryCreate) -> Category:
        category = Category(**data.model_dump())
        return await self.repo.create(category)

    async def update(self, category_id: int, data: CategoryUpdate) -> Category:
        category = await self.get_by_id(category_id)
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(category, field, value)
        await self.repo.db.flush()
        return category

    async def delete(self, category_id: int) -> None:
        category = await self.get_by_id(category_id)
        await self.repo.delete(category)
