from dto.board_dto import get_board_dto
from src.repositories.board_repository import get_board_repository
from src.schemas.board_schemas import get_board_schemas
from src.services.base import BaseService


class BoardService(BaseService):
    pass


def get_board_service() -> BoardService:
    return BoardService(
        repository=get_board_repository(),
        schemas=get_board_schemas(),
        dto=get_board_dto(),
    )
