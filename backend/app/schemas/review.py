from datetime import datetime

from pydantic import BaseModel, field_validator

from app.schemas.user import UserResponse


class ReviewCreate(BaseModel):
    menu_item_id: int
    rating: int
    text: str | None = None

    @field_validator("rating")
    @classmethod
    def validate_rating(cls, v: int) -> int:
        if not 1 <= v <= 5:
            raise ValueError("Рейтинг должен быть от 1 до 5")
        return v


class ReviewMenuItemResponse(BaseModel):
    id: int
    name: str

    model_config = {"from_attributes": True}


class ReviewResponse(BaseModel):
    id: int
    user_id: int
    menu_item_id: int
    rating: int
    text: str | None
    created_at: datetime
    user: UserResponse | None = None
    menu_item: ReviewMenuItemResponse | None = None

    model_config = {"from_attributes": True}
