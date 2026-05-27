from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel

from app.models.order import OrderStatus


class OrderItemResponse(BaseModel):
    id: int
    menu_item_id: int | None
    item_name: str
    price: Decimal
    quantity: int
    subtotal: Decimal

    model_config = {"from_attributes": True}


class OrderUserResponse(BaseModel):
    id: int
    full_name: str
    email: str

    model_config = {"from_attributes": True}


class OrderCreate(BaseModel):
    delivery_type: str = "pickup"
    delivery_address: str | None = None
    comment: str | None = None


class OrderStatusUpdate(BaseModel):
    status: OrderStatus


class OrderResponse(BaseModel):
    id: int
    user_id: int
    status: OrderStatus
    total_amount: Decimal
    delivery_type: str = "pickup"
    delivery_address: str | None = None
    comment: str | None = None
    created_at: datetime
    items: list[OrderItemResponse] = []
    user: OrderUserResponse | None = None

    model_config = {"from_attributes": True}
