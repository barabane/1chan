from src.routers.base import BaseRouter
from src.services.thread_service import get_thread_service


class ThreadRouter(BaseRouter):
    pass


thread_router = ThreadRouter(
    service=get_thread_service(), prefix='/thread', tags=['Thread']
)
