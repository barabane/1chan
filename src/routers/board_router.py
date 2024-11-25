from src.routers.base import BaseRouter
from src.services.board_service import get_board_service


class BoardRouter(BaseRouter):
    pass


board_router = BoardRouter(service=get_board_service(), prefix='/board', tags=['Board'])
