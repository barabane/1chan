import uuid
from datetime import datetime
from typing import Optional

from pydantic import Field

from src.schemas.base import (
    BaseCreateScheme,
    BaseGetScheme,
    BaseSChemas,
    BaseUpdateScheme,
)


class ThreadCreateScheme(BaseCreateScheme):
    title: str = Field(max_length=200)
    text: str = Field(max_length=15000)
    likes_count: Optional[int] = Field(ge=0, default=0)
    dislikes_count: Optional[int] = Field(ge=0, default=0)
    posters_count: Optional[int] = Field(ge=0, default=0)
    posts_count: Optional[int] = Field(ge=0, default=0)
    files_count: Optional[int] = Field(ge=0, default=0)


class ThreadUpdateScheme(BaseUpdateScheme):
    pass


class ThreadGetScheme(BaseGetScheme):
    id: uuid.UUID | str
    number: int = Field(ge=0)
    title: str = Field(max_length=200)
    text: str = Field(max_length=15000)
    likes_count: int = Field(ge=0)
    dislikes_count: int = Field(ge=0)
    posters_count: int = Field(ge=0)
    posts_count: int = Field(ge=0)
    files_count: int = Field(ge=0)
    created_at: datetime


class ThreadSchemas(BaseSChemas):
    create_scheme: ThreadCreateScheme = None
    update_scheme: ThreadUpdateScheme = None
    get_scheme: ThreadGetScheme = None


def get_thread_schemas() -> ThreadSchemas:
    return ThreadSchemas(
        create_scheme=ThreadCreateScheme,
        update_scheme=ThreadUpdateScheme,
        get_scheme=ThreadGetScheme,
    )
