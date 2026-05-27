from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, field_validator

from app.schemas.category import CategoryResponse


class MenuItemCreate(BaseModel):
    name: str
    description: str | None = None
    price: Decimal
    weight_grams: int | None = None
    image_url: str | None = None
    category_id: int
    is_available: bool = True
    is_active: bool = True

    @field_validator("price")
    @classmethod
    def validate_price(cls, v: Decimal) -> Decimal:
        if v <= 0:
            raise ValueError("Цена должна быть больше нуля")
        return v


class MenuItemUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: Decimal | None = None
    weight_grams: int | None = None
    image_url: str | None = None
    category_id: int | None = None
    is_available: bool | None = None
    is_active: bool | None = None


class MenuItemResponse(BaseModel):
    id: int
    name: str
    description: str | None
    price: Decimal
    weight_grams: int | None
    image_url: str | None
    category_id: int
    category: CategoryResponse | None = None
    is_available: bool
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}


class MenuItemListResponse(BaseModel):
    items: list[MenuItemResponse]
    total: int
    skip: int
    limit: int
