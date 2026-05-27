from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependencies import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.favorite import FavoriteResponse
from app.services.favorite import FavoriteService

router = APIRouter()


@router.get("", response_model=list[FavoriteResponse], summary="Избранное пользователя")
async def get_favorites(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = FavoriteService(db)
    return await service.get_favorites(current_user.id)


@router.post("/{menu_item_id}", response_model=FavoriteResponse, status_code=201,
             summary="Добавить в избранное")
async def add_favorite(
    menu_item_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = FavoriteService(db)
    return await service.add_favorite(current_user.id, menu_item_id)


@router.delete("/{menu_item_id}", status_code=204, summary="Удалить из избранного")
async def remove_favorite(
    menu_item_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = FavoriteService(db)
    await service.remove_favorite(current_user.id, menu_item_id)
