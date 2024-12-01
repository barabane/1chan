from src.database.models.file import File
from src.repositories.base import BaseRepository


class FileRepository(BaseRepository):
    pass


def get_file_repository() -> FileRepository:
    return FileRepository(model=File)
