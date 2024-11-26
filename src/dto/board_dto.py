from src.dto.base import BaseCreateDTO, BaseDTO, BaseGetDTO, BaseUpdateDTO
from src.schemas.board_schemas import (
    BoardCreateScheme,
    BoardGetScheme,
    BoardUpdateScheme,
)


class BoardCreateDTO(BaseCreateDTO, BoardCreateScheme):
    pass


class BoardUpdateDTO(BaseUpdateDTO, BoardUpdateScheme):
    pass


class BoardGetDTO(BaseGetDTO, BoardGetScheme):
    pass


class BoardDTO(BaseDTO):
    def __init__(
        self,
        create_dto: BoardCreateDTO = None,
        update_dto: BoardUpdateDTO = None,
        get_dto: BoardGetDTO = None,
    ):
        super().__init__(
            create_dto=create_dto,
            update_dto=update_dto,
            get_dto=get_dto,
        )


def get_board_dto() -> BoardDTO:
    return BoardDTO(
        create_dto=BoardCreateDTO, update_dto=BoardUpdateDTO, get_dto=BoardGetDTO
    )
