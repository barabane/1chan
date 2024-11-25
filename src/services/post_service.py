from src.dto.post_dto import get_post_dto
from src.repositories.post_repository import get_post_repository
from src.schemas.post_schemas import get_post_schemas
from src.services.base import BaseService


class PostService(BaseService):
    pass


def get_post_service() -> PostService:
    return PostService(
        repository=get_post_repository(), schemas=get_post_schemas(), dto=get_post_dto()
    )
