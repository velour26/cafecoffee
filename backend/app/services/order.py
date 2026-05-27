from decimal import Decimal

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.order import Order, OrderStatus
from app.models.order_item import OrderItem
from app.repositories.cart import CartRepository
from app.repositories.order import OrderRepository
from app.schemas.order import OrderCreate, OrderStatusUpdate


class OrderService:
    def __init__(self, db: AsyncSession) -> None:
        self.order_repo = OrderRepository(db)
        self.cart_repo = CartRepository(db)

    async def create_order(self, user_id: int, data: OrderCreate) -> Order:
        cart_items = await self.cart_repo.get_user_cart(user_id)
        if not cart_items:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Корзина пуста. Добавьте позиции перед оформлением заказа.",
            )

        total = Decimal("0.00")
        for item in cart_items:
            if item.menu_item:
                total += item.menu_item.price * item.quantity

        order = Order(
            user_id=user_id,
            status=OrderStatus.NEW,
            total_amount=total,
            delivery_type=data.delivery_type,
            delivery_address=data.delivery_address,
            comment=data.comment,
        )
        await self.order_repo.create(order)

        for cart_item in cart_items:
            if cart_item.menu_item:
                order_item = OrderItem(
                    order_id=order.id,
                    menu_item_id=cart_item.menu_item_id,
                    item_name=cart_item.menu_item.name,
                    price=cart_item.menu_item.price,
                    quantity=cart_item.quantity,
                    subtotal=cart_item.menu_item.price * cart_item.quantity,
                )
                self.order_repo.db.add(order_item)

        await self.cart_repo.clear_user_cart(user_id)
        await self.order_repo.db.flush()
        return await self.order_repo.get_order_with_items(order.id)

    async def get_user_orders(self, user_id: int, skip: int = 0, limit: int = 20) -> list[Order]:
        return await self.order_repo.get_user_orders(user_id, skip, limit)

    async def get_order(self, order_id: int, user_id: int | None = None) -> Order:
        order = await self.order_repo.get_order_with_items(order_id)
        if not order:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Заказ не найден"
            )
        if user_id is not None and order.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Нет доступа к этому заказу"
            )
        return order

    async def get_all_orders(self, skip: int = 0, limit: int = 50) -> list[Order]:
        return await self.order_repo.get_all_orders(skip, limit)

    async def update_status(self, order_id: int, data: OrderStatusUpdate) -> Order:
        order = await self.order_repo.get_order_with_items(order_id)
        if not order:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Заказ не найден"
            )
        order.status = data.status
        await self.order_repo.db.flush()
        return order
