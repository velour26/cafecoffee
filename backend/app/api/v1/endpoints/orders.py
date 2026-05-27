from fastapi import APIRouter, Body, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependencies import get_admin_user, get_current_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.order import OrderCreate, OrderResponse, OrderStatusUpdate
from app.services.order import OrderService

router = APIRouter()


@router.post("", response_model=OrderResponse, status_code=201, summary="Оформить заказ")
async def create_order(
    data: OrderCreate = Body(default=OrderCreate()),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = OrderService(db)
    return await service.create_order(current_user.id, data)


@router.get("/my", response_model=list[OrderResponse], summary="Мои заказы")
async def get_my_orders(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = OrderService(db)
    return await service.get_user_orders(current_user.id, skip, limit)


@router.get("", response_model=list[OrderResponse], summary="Все заказы (admin)")
async def get_all_orders(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    db: AsyncSession = Depends(get_db),
    _admin: User = Depends(get_admin_user),
):
    service = OrderService(db)
    return await service.get_all_orders(skip, limit)


@router.get("/{order_id}", response_model=OrderResponse, summary="Заказ по ID")
async def get_order(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = OrderService(db)
    is_admin = current_user.role and current_user.role.name == "admin"
    return await service.get_order(
        order_id, user_id=None if is_admin else current_user.id
    )


@router.put("/{order_id}/status", response_model=OrderResponse,
            summary="Изменить статус заказа (admin)")
async def update_order_status(
    order_id: int,
    data: OrderStatusUpdate,
    db: AsyncSession = Depends(get_db),
    _admin: User = Depends(get_admin_user),
):
    service = OrderService(db)
    return await service.update_status(order_id, data)
