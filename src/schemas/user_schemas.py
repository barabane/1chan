from src.schemas.base import (
    BaseCreateScheme,
    BaseGetScheme,
    BaseSChemas,
    BaseUpdateScheme,
)


class UserCreateScheme(BaseCreateScheme):
    pass


class UserUpdateScheme(BaseUpdateScheme):
    pass


class UserGetScheme(BaseGetScheme):
    pass


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
