import uuid
from typing import Annotated, List

from pydantic import AfterValidator, Field

from src.schemas.base import (
    BaseCreateScheme,
    BaseGetScheme,
    BaseSChemas,
    BaseUpdateScheme,
)


def validate_tag(tag: str) -> str:
    if not tag.startswith('#'):
        assert tag, ' should start with #'
    return tag


BoardTag = Annotated[str, AfterValidator(validate_tag)]


class BoardCreateScheme(BaseCreateScheme):
    link: str = Field(max_length=8, min_length=3)
    name: str = Field(max_length=50, min_length=3)
    description: str = Field(max_length=2000)
    tags: List[BoardTag] = Field(default=[])


class BoardUpdateScheme(BaseUpdateScheme):
    pass


class BoardGetScheme(BaseGetScheme):
    id: uuid.UUID | str
    link: str = Field(max_length=8, min_length=3)
    name: str = Field(max_length=50, min_length=3)
    description: str = Field(max_length=2000)
    tags: List[BoardTag] = Field(default=[])


class BoardSchemas(BaseSChemas):
    def __init__(
        self,
        create_scheme: BoardCreateScheme = None,
        update_scheme: BoardUpdateScheme = None,
        get_scheme: BoardGetScheme = None,
    ):
        super().__init__(
            create_scheme=create_scheme,
            update_scheme=update_scheme,
            get_scheme=get_scheme,
        )


def get_board_schemas() -> BoardSchemas:
    return BoardSchemas(
        create_scheme=BoardCreateScheme,
        update_scheme=BoardUpdateScheme,
        get_scheme=BoardGetScheme,
    )
