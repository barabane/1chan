from typing import List, Literal

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.database import get_async_session
from src.dto.thread_dto import get_thread_dto
from src.repositories.thread_repository import get_thread_repository
from src.schemas.thread_schemas import ThreadGetScheme, get_thread_schemas
from src.services.base import BaseService


class ThreadService(BaseService):
    async def get_top_threads(
        self,
        by: Literal['time', 'comments'],
        limit: int = 20,
        session: AsyncSession = Depends(get_async_session),
    ) -> List[ThreadGetScheme]:
        top_threads = await self.repository.get_top_threads(
            by=by, limit=limit, session=session
        )

        return [
            await self.get_by_id(thread.id, session=session) for thread in top_threads
        ]

    async def get_local_top(
        self,
        board_id: str,
        by: Literal['time', 'comments'],
        limit: int = 20,
        session: AsyncSession = Depends(get_async_session),
    ):
        local_top_threads = await self.repository.get_top_threads(
            board_id=board_id, by=by, limit=limit, session=session
        )

        return [
            await self.get_by_id(thread.id, session=session)
            for thread in local_top_threads
        ]

    async def like_thread(
        self, thread_id: str, session: AsyncSession = Depends(get_async_session)
    ) -> None:
        await self.repository.like_thread(thread_id=thread_id, session=session)

    async def dislike_thread(
        self, thread_id: str, session: AsyncSession = Depends(get_async_session)
    ) -> None:
        await self.repository.dislike_thread(thread_id=thread_id, session=session)


def get_thread_service() -> ThreadService:
    return ThreadService(
        repository=get_thread_repository(),
        schemas=get_thread_schemas(),
        dto=get_thread_dto(),
    )
