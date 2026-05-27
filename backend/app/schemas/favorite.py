from datetime import datetime

from pydantic import BaseModel

from app.schemas.menu_item import MenuItemResponse


class FavoriteResponse(BaseModel):
    id: int
    user_id: int
    menu_item_id: int
    menu_item: MenuItemResponse | None = None
    created_at: datetime

    model_config = {"from_attributes": True}
