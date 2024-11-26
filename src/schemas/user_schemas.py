import uuid
from typing import Optional

from pydantic import Field

from src.schemas.base import (
    BaseCreateScheme,
    BaseGetScheme,
    BaseSChemas,
    BaseUpdateScheme,
)


class UserCreateScheme(BaseCreateScheme):
    email: Optional[str] = Field(max_length=50, default=None)
    ip_address: Optional[str] = Field(max_length=15)


class UserUpdateScheme(BaseUpdateScheme):
    pass


class UserGetScheme(BaseGetScheme):
    id: uuid.UUID | str
    email: Optional[str] = Field(max_length=50, default=None)
    ip_address: Optional[str] = Field(max_length=15)


class UserSchemas(BaseSChemas):
    def __init__(
        self,
        create_scheme: UserCreateScheme = None,
        update_scheme: UserUpdateScheme = None,
        get_scheme: UserGetScheme = None,
    ):
        super().__init__(
            create_scheme=create_scheme,
            update_scheme=update_scheme,
            get_scheme=get_scheme,
        )


def get_user_schemas():
    return UserSchemas(
        create_scheme=UserCreateScheme,
        update_scheme=UserUpdateScheme,
        get_scheme=UserGetScheme,
    )
