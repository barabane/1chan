import uuid
from datetime import datetime

from pydantic import Field

from src.schemas.base import (
    BaseCreateScheme,
    BaseGetScheme,
    BaseSChemas,
    BaseUpdateScheme,
)


class PostCreateScheme(BaseCreateScheme):
    author_id: str
    text: str = Field(max_length=15000)


class PostUpdateScheme(BaseUpdateScheme):
    pass


class PostGetScheme(BaseGetScheme):
    id: uuid.UUID | str
    number: int = Field(ge=0)
    author_id: str
    text: str = Field(max_length=15000)
    created_at: datetime


class PostSchemas(BaseSChemas):
    def __init__(
        self,
        create_scheme: PostCreateScheme = None,
        update_scheme: PostUpdateScheme = None,
        get_scheme: PostGetScheme = None,
    ):
        super().__init__(
            create_scheme=create_scheme,
            update_scheme=update_scheme,
            get_scheme=get_scheme,
        )


def get_post_schemas() -> PostSchemas:
    return PostSchemas(
        create_scheme=PostCreateScheme,
        update_scheme=PostUpdateScheme,
        get_scheme=PostGetScheme,
    )
