from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.review import Review
from app.repositories.menu_item import MenuItemRepository
from app.repositories.review import ReviewRepository
from app.schemas.review import ReviewCreate


class ReviewService:
    def __init__(self, db: AsyncSession) -> None:
        self.review_repo = ReviewRepository(db)
        self.menu_repo = MenuItemRepository(db)
        self.db = db

    async def create_review(self, user_id: int, data: ReviewCreate) -> Review:
        menu_item = await self.menu_repo.get_by_id(data.menu_item_id)
        if not menu_item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Позиция меню не найдена"
            )

        result = await self.db.execute(
            select(OrderItem.id)
            .join(Order, OrderItem.order_id == Order.id)
            .where(
                Order.user_id == user_id,
                OrderItem.menu_item_id == data.menu_item_id,
            )
            .limit(1)
        )
        ordered_item = result.scalar_one_or_none()
        if not ordered_item:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Отзыв можно оставить только на позиции, которые вы заказывали",
            )

        existing = await self.review_repo.get_user_review_for_item(user_id, data.menu_item_id)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Вы уже оставили отзыв на эту позицию",
            )

        review = Review(
            user_id=user_id,
            menu_item_id=data.menu_item_id,
            rating=data.rating,
            text=data.text,
        )
        return await self.review_repo.create(review)

    async def get_all_reviews(self, skip: int = 0, limit: int = 50) -> list[Review]:
        return await self.review_repo.get_all_reviews(skip, limit)

    async def delete_review(self, review_id: int) -> None:
        review = await self.review_repo.get_by_id(review_id)
        if not review:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Отзыв не найден")
        await self.review_repo.delete(review)

    async def get_by_menu_item(self, menu_item_id: int) -> list[Review]:
        return await self.review_repo.get_by_menu_item(menu_item_id)
