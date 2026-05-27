from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependencies import get_current_user
from app.core.security import get_password_hash
from app.db.session import get_db
from app.models.user import User
from app.repositories.user import UserRepository
from app.schemas.auth import LoginRequest, RegisterRequest, TokenResponse
from app.schemas.user import PasswordChange, UserResponse, UserUpdate
from app.services.auth import AuthService

router = APIRouter()


@router.post("/register", response_model=UserResponse, status_code=201,
             summary="Регистрация нового пользователя")
async def register(data: RegisterRequest, db: AsyncSession = Depends(get_db)):
    service = AuthService(db)
    return await service.register(data)


@router.post("/login", response_model=TokenResponse, summary="Вход в систему")
async def login(data: LoginRequest, db: AsyncSession = Depends(get_db)):
    service = AuthService(db)
    return await service.login(data)


@router.get("/me", response_model=UserResponse, summary="Текущий пользователь")
async def me(current_user: User = Depends(get_current_user)):
    return current_user


@router.put("/me", response_model=UserResponse, summary="Обновить профиль")
async def update_me(
    data: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    repo = UserRepository(db)
    if data.email and data.email != current_user.email:
        existing = await repo.get_by_email(data.email)
        if existing:
            raise HTTPException(status_code=400, detail="Email уже занят")
    update_data = data.model_dump(exclude_none=True)
    for key, value in update_data.items():
        setattr(current_user, key, value)
    return await repo.update(current_user)


@router.put("/me/password", summary="Сменить пароль")
async def change_password(
    data: PasswordChange,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    if len(data.password) < 6:
        raise HTTPException(status_code=400, detail="Пароль должен быть не менее 6 символов")
    repo = UserRepository(db)
    current_user.hashed_password = get_password_hash(data.password)
    await repo.update(current_user)
    return {"detail": "Пароль изменён"}
