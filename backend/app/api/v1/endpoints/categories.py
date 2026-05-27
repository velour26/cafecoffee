from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependencies import get_admin_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.category import CategoryCreate, CategoryResponse, CategoryUpdate
from app.services.category import CategoryService

router = APIRouter()


@router.get("", response_model=list[CategoryResponse], summary="Список категорий")
async def get_categories(db: AsyncSession = Depends(get_db)):
    service = CategoryService(db)
    return await service.get_all()


@router.get("/{category_id}", response_model=CategoryResponse, summary="Категория по ID")
async def get_category(category_id: int, db: AsyncSession = Depends(get_db)):
    service = CategoryService(db)
    return await service.get_by_id(category_id)


@router.post("", response_model=CategoryResponse, status_code=201,
             summary="Создать категорию (admin)")
async def create_category(
    data: CategoryCreate,
    db: AsyncSession = Depends(get_db),
    _admin: User = Depends(get_admin_user),
):
    service = CategoryService(db)
    return await service.create(data)


@router.put("/{category_id}", response_model=CategoryResponse,
            summary="Обновить категорию (admin)")
async def update_category(
    category_id: int,
    data: CategoryUpdate,
    db: AsyncSession = Depends(get_db),
    _admin: User = Depends(get_admin_user),
):
    service = CategoryService(db)
    return await service.update(category_id, data)


@router.delete("/{category_id}", status_code=204, summary="Удалить категорию (admin)")
async def delete_category(
    category_id: int,
    db: AsyncSession = Depends(get_db),
    _admin: User = Depends(get_admin_user),
):
    service = CategoryService(db)
    await service.delete(category_id)
