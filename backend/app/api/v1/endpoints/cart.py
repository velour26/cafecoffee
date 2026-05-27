from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependencies import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.cart import CartItemCreate, CartItemResponse, CartItemUpdate, CartResponse
from app.services.cart import CartService

router = APIRouter()


@router.get("", response_model=CartResponse, summary="Корзина текущего пользователя")
async def get_cart(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = CartService(db)
    return await service.get_cart(current_user.id)


@router.post("", response_model=CartItemResponse, status_code=201,
             summary="Добавить позицию в корзину")
async def add_to_cart(
    data: CartItemCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = CartService(db)
    return await service.add_to_cart(current_user.id, data)


@router.put("/{item_id}", response_model=CartItemResponse | None,
            summary="Обновить количество в корзине")
async def update_cart_item(
    item_id: int,
    data: CartItemUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = CartService(db)
    return await service.update_cart_item(current_user.id, item_id, data)


@router.delete("/clear", status_code=204, summary="Очистить корзину")
async def clear_cart(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = CartService(db)
    await service.clear_cart(current_user.id)


@router.delete("/{item_id}", status_code=204, summary="Удалить позицию из корзины")
async def remove_from_cart(
    item_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = CartService(db)
    await service.remove_from_cart(current_user.id, item_id)
