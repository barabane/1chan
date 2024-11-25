from src.database.models.user import User
from src.repositories.base import BaseRepository


class UserRepository(BaseRepository):
    pass


def get_user_repository() -> UserRepository:
    return UserRepository(model=User)
