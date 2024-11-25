from src.dto.thread_dto import get_thread_dto
from src.repositories.thread_repository import get_thread_repository
from src.schemas.thread_schemas import get_thread_schemas
from src.services.base import BaseService


class ThreadService(BaseService):
    pass


def get_thread_service() -> ThreadService:
    return ThreadService(
        repository=get_thread_repository(),
        schemas=get_thread_schemas(),
        dto=get_thread_dto(),
    )
