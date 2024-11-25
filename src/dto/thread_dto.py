from src.dto.base import BaseCreateDTO, BaseDTO, BaseGetDTO, BaseUpdateDTO
from src.schemas.thread_schemas import (
    ThreadCreateScheme,
    ThreadGetScheme,
    ThreadUpdateScheme,
)


class ThreadCreateDTO(BaseCreateDTO, ThreadCreateScheme):
    pass


class ThreadUpdateDTO(BaseUpdateDTO, ThreadUpdateScheme):
    pass


class ThreadGetDTO(BaseGetDTO, ThreadGetScheme):
    pass


class ThreadDTO(BaseDTO):
    def __init__(
        self,
        create_dto: ThreadCreateDTO = None,
        update_dto: ThreadUpdateDTO = None,
        get_dto: ThreadGetDTO = None,
    ):
        super().__init__(
            create_dto=create_dto,
            update_dto=update_dto,
            get_dto=get_dto,
        )


def get_thread_dto() -> ThreadDTO:
    return ThreadDTO(
        create_dto=ThreadCreateDTO,
        update_dto=ThreadUpdateDTO,
        get_dto=ThreadGetDTO,
    )
