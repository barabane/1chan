from src.database.models.thread import Thread
from src.repositories.base import BaseRepository


class ThreadRepository(BaseRepository):
    pass


def get_thread_repository() -> ThreadRepository:
    return ThreadRepository(model=Thread)
