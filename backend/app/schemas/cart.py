from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, field_validator

from app.schemas.menu_item import MenuItemResponse


class CartItemCreate(BaseModel):
    menu_item_id: int
    quantity: int = 1

    @field_validator("quantity")
    @classmethod
    def validate_qty(cls, v: int) -> int:
        if v < 1:
            raise ValueError("Количество должно быть не менее 1")
        return v


class CartItemUpdate(BaseModel):
    quantity: int

    @field_validator("quantity")
    @classmethod
    def validate_qty(cls, v: int) -> int:
        if v < 0:
            raise ValueError("Количество не может быть отрицательным")
        return v


class CartItemResponse(BaseModel):
    id: int
    user_id: int
    menu_item_id: int
    menu_item: MenuItemResponse | None = None
    quantity: int
    created_at: datetime

    model_config = {"from_attributes": True}


class CartResponse(BaseModel):
    items: list[CartItemResponse]
    total: Decimal
