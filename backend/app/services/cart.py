from decimal import Decimal

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.cart_item import CartItem
from app.repositories.cart import CartRepository
from app.repositories.menu_item import MenuItemRepository
from app.schemas.cart import CartItemCreate, CartItemUpdate, CartResponse


class CartService:
    def __init__(self, db: AsyncSession) -> None:
        self.cart_repo = CartRepository(db)
        self.menu_repo = MenuItemRepository(db)

    async def get_cart(self, user_id: int) -> CartResponse:
        items = await self.cart_repo.get_user_cart(user_id)
        total = Decimal("0.00")
        for item in items:
            if item.menu_item:
                total += item.menu_item.price * item.quantity
        return CartResponse(items=items, total=total)

    async def add_to_cart(self, user_id: int, data: CartItemCreate) -> CartItem:
        menu_item = await self.menu_repo.get_by_id(data.menu_item_id)
        if not menu_item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Позиция меню не найдена"
            )
        if not menu_item.is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Позиция меню удалена"
            )
        if not menu_item.is_available:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Позиция временно недоступна"
            )

        existing = await self.cart_repo.get_existing_item(user_id, data.menu_item_id)
        if existing:
            existing.quantity += data.quantity
            await self.cart_repo.db.flush()
            return existing

        cart_item = CartItem(
            user_id=user_id,
            menu_item_id=data.menu_item_id,
            quantity=data.quantity,
        )
        return await self.cart_repo.create(cart_item)

    async def update_cart_item(
        self, user_id: int, item_id: int, data: CartItemUpdate
    ) -> CartItem | None:
        item = await self.cart_repo.get_user_cart_item(user_id, item_id)
        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Элемент корзины не найден"
            )
        if data.quantity == 0:
            await self.cart_repo.delete(item)
            return None
        item.quantity = data.quantity
        await self.cart_repo.db.flush()
        return item

    async def remove_from_cart(self, user_id: int, item_id: int) -> None:
        item = await self.cart_repo.get_user_cart_item(user_id, item_id)
        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Элемент корзины не найден"
            )
        await self.cart_repo.delete(item)

    async def clear_cart(self, user_id: int) -> None:
        await self.cart_repo.clear_user_cart(user_id)
