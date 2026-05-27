from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependencies import get_admin_user
from app.db.session import get_db
from app.models.contact_message import ContactMessage
from app.models.user import User
from app.schemas.contact_message import ContactMessageCreate, ContactMessageResponse

router = APIRouter()


@router.post(
    "",
    response_model=ContactMessageResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Отправить сообщение (публичный)",
)
async def create_contact_message(
    data: ContactMessageCreate,
    db: AsyncSession = Depends(get_db),
):
    msg = ContactMessage(
        name=data.name,
        email=data.email,
        topic=data.topic or None,
        message=data.message,
    )
    db.add(msg)
    await db.commit()
    await db.refresh(msg)
    return msg


@router.get(
    "",
    response_model=list[ContactMessageResponse],
    summary="Список сообщений (admin)",
)
async def get_contact_messages(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: AsyncSession = Depends(get_db),
    _admin: User = Depends(get_admin_user),
):
    result = await db.execute(
        select(ContactMessage)
        .order_by(ContactMessage.created_at.desc())
        .offset(skip)
        .limit(limit)
    )
    return result.scalars().all()


@router.patch(
    "/{msg_id}/read",
    response_model=ContactMessageResponse,
    summary="Пометить как прочитанное (admin)",
)
async def mark_as_read(
    msg_id: int,
    db: AsyncSession = Depends(get_db),
    _admin: User = Depends(get_admin_user),
):
    result = await db.execute(select(ContactMessage).where(ContactMessage.id == msg_id))
    msg = result.scalar_one_or_none()
    if not msg:
        raise HTTPException(status_code=404, detail="Сообщение не найдено")
    msg.is_read = True
    await db.commit()
    await db.refresh(msg)
    return msg


@router.delete(
    "/{msg_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удалить сообщение (admin)",
)
async def delete_contact_message(
    msg_id: int,
    db: AsyncSession = Depends(get_db),
    _admin: User = Depends(get_admin_user),
):
    result = await db.execute(
        delete(ContactMessage).where(ContactMessage.id == msg_id)
    )
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Сообщение не найдено")
