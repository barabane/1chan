import uuid
from typing import List

from fastapi import Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.database import get_async_session
from src.database.models.post import Post
from src.dto.file_dto import FileCreateDTO
from src.dto.post_dto import PostCreateDTO, PostDTO, get_post_dto
from src.exceptions import (
    FilesTotalSizeTooLarge,
    InternalServerErrorException,
    TooManyFilesException,
)
from src.repositories.post_repository import PostRepository, get_post_repository
from src.schemas.base import BaseSChemas
from src.schemas.file_schemas import FileGetScheme
from src.schemas.post_schemas import get_post_schemas
from src.services.base import BaseService
from src.services.file_service import FileService, get_file_service
from src.utils.s3_client import s3_client


class PostService(BaseService):
    def __init__(
        self,
        repository: PostRepository,
        schemas: BaseSChemas,
        dto: PostDTO,
        file_service: FileService,
    ) -> None:
        super().__init__(repository, schemas, dto)
        self.file_service = file_service

    async def add(
        self,
        post_dto: PostCreateDTO,
        session: AsyncSession = Depends(get_async_session),
    ):
        post_model: Post = await self.repository.add(entity=post_dto, session=session)
        return self.schemas.get_scheme(**post_model.__dict__)

    async def add_files(
        self,
        post_id: str,
        files: List[UploadFile],
        session: AsyncSession = Depends(get_async_session),
    ) -> List[str]:
        post_files: List[FileGetScheme] = await self.file_service.get_all(
            query_params={'post_id': post_id}, session=session
        )

        if len(post_files) + len(files) > 4:
            raise TooManyFilesException()

        file_sizes = [file.size for file in files]

        if sum(file_sizes) > 1048576:
            raise FilesTotalSizeTooLarge()

        try:
            links = []
            for file in files:
                file_name = str(uuid.uuid4())
                file_link = await s3_client.upload_file(
                    file=file.file, file_name=file_name
                )
                links.append(file_link)

                file_dto = FileCreateDTO(
                    id=file_name,
                    name=file_name,
                    link=file_link,
                    size=file.size,
                    post_id=post_id,
                )
            await self.file_service.add(entity=file_dto, session=session)
            return links
        except Exception as ex:
            await session.rollback()
            [await s3_client.delete_file(link.split('/')[-1]) for link in links]
            raise InternalServerErrorException(detail=str(ex))


def get_post_service() -> PostService:
    return PostService(
        repository=get_post_repository(),
        schemas=get_post_schemas(),
        dto=get_post_dto(),
        file_service=get_file_service(),
    )
