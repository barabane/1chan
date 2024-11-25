from src.dto.base import BaseCreateDTO, BaseGetDTO, BaseUpdateDTO
from src.schemas.board_schemas import (
    BoardCreateScheme,
    BoardGetScheme,
    BoardUpdateScheme,
)


def validate_tag(tag: str) -> str:
    if not tag.startswith('#'):
        assert tag, ' should start with #'
    return tag


# BoardTag = Annotated[str, AfterValidator(validate_tag)]


class BoardCreateDTO(BaseCreateDTO, BoardCreateScheme):
    pass


class BoardUpdateDTO(BaseUpdateDTO, BoardUpdateScheme):
    pass


class BoardGetDTO(BaseGetDTO, BoardGetScheme):
    pass


class BoardDTO:
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
    return BoardDTO()
