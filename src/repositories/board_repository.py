from src.database.models.board import Board
from src.repositories.base import BaseRepository


class BoardRepository(BaseRepository):
    pass


def get_board_repository() -> BoardRepository:
    return BoardRepository(model=Board)
