from typing import List

from fastapi import Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.database import get_async_session
from src.database.models.post import Post
from src.dto.post_dto import PostCreateDTO, get_post_dto
from src.repositories.post_repository import get_post_repository
from src.schemas.post_schemas import get_post_schemas
from src.services.base import BaseService


class PostService(BaseService):
    async def add(
        self,
        post_dto: PostCreateDTO,
        files: List[UploadFile],
        session: AsyncSession = Depends(get_async_session),
    ):
        post_model: Post = await self.repository.add(entity=post_dto, session=session)

        return self.schemas.get_scheme(**post_model.__dict__)


def get_post_service() -> PostService:
    return PostService(
        repository=get_post_repository(), schemas=get_post_schemas(), dto=get_post_dto()
    )
