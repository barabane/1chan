from typing import List, Literal

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models.thread import Thread
from src.repositories.base import BaseRepository


class ThreadRepository(BaseRepository):
    async def get_top_threads(
        self,
        by: Literal['time', 'posts'],
        session: AsyncSession,
        limit: int = 20,
        board_id: str = None,
    ) -> List[Thread]:
        if by == 'time' and board_id:
            query = (
                select(Thread)
                .where(Thread.board_id == board_id)
                .order_by(Thread.created_at.desc())
                .limit(limit)
            )
        else:
            query = select(Thread).order_by(Thread.created_at.desc()).limit(limit)

        top_threads = await session.execute(query)
        return top_threads.scalars().all()

    async def like_thread(self, thread_id: str, session: AsyncSession):
        query = (
            update(Thread)
            .where(Thread.id == thread_id)
            .values(likes_count=Thread.likes_count + 1)
        )
        await session.execute(query)

    async def dislike_thread(self, thread_id: str, session: AsyncSession):
        query = (
            update(Thread)
            .where(Thread.id == thread_id)
            .values(dislikes_count=Thread.dislikes_count + 1)
        )
        await session.execute(query)


def get_thread_repository() -> ThreadRepository:
    return ThreadRepository(model=Thread)
