from datetime import datetime

from pydantic import BaseModel, EmailStr, field_validator


class ContactMessageCreate(BaseModel):
    name: str
    email: EmailStr
    topic: str | None = None
    message: str

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Имя не может быть пустым")
        if len(v) > 100:
            raise ValueError("Имя не должно превышать 100 символов")
        return v

    @field_validator("message")
    @classmethod
    def validate_message(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Сообщение не может быть пустым")
        return v


class ContactMessageResponse(BaseModel):
    id: int
    name: str
    email: str
    topic: str | None
    message: str
    is_read: bool
    created_at: datetime

    model_config = {"from_attributes": True}
