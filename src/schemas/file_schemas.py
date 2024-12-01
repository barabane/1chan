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


class FileCreateScheme(BaseCreateScheme):
    name: str
    link: str
    size: float = Field(ge=0.0)
    width: Optional[int] = Field(ge=0)
    height: Optional[int] = Field(ge=0)
    post_id: uuid.UUID | str


class FileUpdateScheme(BaseUpdateScheme):
    pass


class FileGetScheme(BaseGetScheme):
    id: uuid.UUID | str
    name: str
    link: str
    size: float = Field(ge=0.0)
    created_at: datetime
    width: Optional[int] = Field(ge=0)
    height: Optional[int] = Field(ge=0)
    post_id: uuid.UUID | str


class FileSchemas(BaseSChemas):
    def __init__(
        self,
        create_scheme: FileCreateScheme = None,
        update_scheme: FileUpdateScheme = None,
        get_scheme: FileGetScheme = None,
    ):
        super().__init__(
            create_scheme=create_scheme,
            update_scheme=update_scheme,
            get_scheme=get_scheme,
        )


def get_file_schemas() -> FileSchemas:
    return FileSchemas(
        create_scheme=FileCreateScheme,
        update_scheme=FileUpdateScheme,
        get_scheme=FileGetScheme,
    )
