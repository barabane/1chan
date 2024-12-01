import uuid

from src.dto.base import BaseCreateDTO, BaseDTO, BaseGetDTO, BaseUpdateDTO
from src.schemas.file_schemas import FileCreateScheme, FileGetScheme, FileUpdateScheme


class FileCreateDTO(BaseCreateDTO, FileCreateScheme):
    id: uuid.UUID | str


class FileUpdateDTO(BaseUpdateDTO, FileUpdateScheme):
    pass


class FileGetDTO(BaseGetDTO, FileGetScheme):
    pass


class FileDTO(BaseDTO):
    def __init__(
        self,
        create_dto: FileCreateDTO = None,
        update_dto: FileUpdateDTO = None,
        get_dto: FileGetDTO = None,
    ):
        super().__init__(
            create_dto=create_dto,
            update_dto=update_dto,
            get_dto=get_dto,
        )


def get_file_dto() -> FileDTO:
    return FileDTO(
        create_dto=FileCreateDTO, update_dto=FileUpdateDTO, get_dto=FileGetDTO
    )
