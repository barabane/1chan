from src.dto.base import (
    BaseCreateDTO,
    BaseDTO,
    BaseGetDTO,
    BaseUpdateDTO,
)
from src.schemas.user_schemas import UserCreateScheme, UserGetScheme, UserUpdateScheme


class UserCreateDTO(BaseCreateDTO, UserCreateScheme):
    pass


class UserUpdateDTO(BaseUpdateDTO, UserUpdateScheme):
    pass


class UserGetDTO(BaseGetDTO, UserGetScheme):
    pass


class UserDTO(BaseDTO):
    def __init__(
        self,
        create_dto: UserCreateDTO = None,
        update_dto: UserUpdateDTO = None,
        get_dto: UserGetDTO = None,
    ):
        super().__init__(
            create_dto=create_dto,
            update_dto=update_dto,
            get_dto=get_dto,
        )


def get_user_dto() -> UserDTO:
    return UserDTO(
        create_dto=UserCreateDTO,
        update_dto=UserUpdateDTO,
        get_dto=UserGetDTO,
    )
