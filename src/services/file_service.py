from src.dto.file_dto import get_file_dto
from src.repositories.file_repository import get_file_repository
from src.schemas.file_schemas import get_file_schemas
from src.services.base import BaseService


class FileService(BaseService):
    pass


def get_file_service() -> FileService:
    return FileService(
        repository=get_file_repository(), dto=get_file_dto(), schemas=get_file_schemas()
    )
