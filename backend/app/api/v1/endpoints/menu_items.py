from decimal import Decimal
from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependencies import get_admin_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.menu_item import MenuItemCreate, MenuItemListResponse, MenuItemResponse, MenuItemUpdate
from app.schemas.review import ReviewResponse
from app.services.menu_item import MenuItemService
from app.services.review import ReviewService

router = APIRouter()


@router.get("", response_model=MenuItemListResponse, summary="Список позиций меню с фильтрацией и пагинацией")
async def get_menu_items(
    category_id: Optional[int] = Query(None, description="Фильтр по категории"),
    search: Optional[str] = Query(None, description="Поиск по названию"),
    min_price: Optional[Decimal] = Query(None, description="Минимальная цена"),
    max_price: Optional[Decimal] = Query(None, description="Максимальная цена"),
    include_inactive: bool = Query(False, description="Включая недоступные"),
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=500),
    db: AsyncSession = Depends(get_db),
):
    service = MenuItemService(db)
    return await service.get_filtered(
        category_id=category_id,
        search=search,
        min_price=min_price,
        max_price=max_price,
        skip=skip,
        limit=limit,
        include_inactive=include_inactive,
    )


@router.get("/{item_id}", response_model=MenuItemResponse, summary="Позиция меню по ID")
async def get_menu_item(item_id: int, db: AsyncSession = Depends(get_db)):
    service = MenuItemService(db)
    return await service.get_by_id(item_id)


@router.post("", response_model=MenuItemResponse, status_code=201,
             summary="Создать позицию меню (admin)")
async def create_menu_item(
    data: MenuItemCreate,
    db: AsyncSession = Depends(get_db),
    _admin: User = Depends(get_admin_user),
):
    service = MenuItemService(db)
    return await service.create(data)


@router.put("/{item_id}", response_model=MenuItemResponse,
            summary="Обновить позицию меню (admin)")
async def update_menu_item(
    item_id: int,
    data: MenuItemUpdate,
    db: AsyncSession = Depends(get_db),
    _admin: User = Depends(get_admin_user),
):
    service = MenuItemService(db)
    return await service.update(item_id, data)


@router.delete("/{item_id}", status_code=204,
               summary="Удалить позицию меню (admin, soft delete)")
async def delete_menu_item(
    item_id: int,
    db: AsyncSession = Depends(get_db),
    _admin: User = Depends(get_admin_user),
):
    service = MenuItemService(db)
    await service.delete(item_id)


@router.get("/{item_id}/reviews", response_model=list[ReviewResponse],
            summary="Отзывы на позицию меню")
async def get_item_reviews(item_id: int, db: AsyncSession = Depends(get_db)):
    service = ReviewService(db)
    return await service.get_by_menu_item(item_id)
