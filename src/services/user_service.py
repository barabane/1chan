from src.dto.user_dto import get_user_dto
from src.repositories.user_repository import get_user_repository
from src.schemas.user_schemas import get_user_schemas
from src.services.base import BaseService


class UserService(BaseService):
    pass


def get_user_service() -> UserService:
    return UserService(
        repository=get_user_repository(), schemas=get_user_schemas(), dto=get_user_dto()
    )
