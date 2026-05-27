from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependencies import get_admin_user, get_current_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.review import ReviewCreate, ReviewResponse
from app.services.review import ReviewService

router = APIRouter()


@router.get("", response_model=list[ReviewResponse], summary="Все отзывы")
async def get_reviews(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    db: AsyncSession = Depends(get_db),
):
    service = ReviewService(db)
    return await service.get_all_reviews(skip, limit)


@router.post("", response_model=ReviewResponse, status_code=201, summary="Оставить отзыв")
async def create_review(
    data: ReviewCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ReviewService(db)
    return await service.create_review(current_user.id, data)


@router.delete("/{review_id}", status_code=204, summary="Удалить отзыв (admin)")
async def delete_review(
    review_id: int,
    db: AsyncSession = Depends(get_db),
    _admin: User = Depends(get_admin_user),
):
    service = ReviewService(db)
    await service.delete_review(review_id)
