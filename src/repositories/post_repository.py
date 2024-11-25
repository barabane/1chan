from src.database.models.post import Post
from src.repositories.base import BaseRepository


class PostRepository(BaseRepository):
    pass


def get_post_repository() -> PostRepository:
    return PostRepository(model=Post)
