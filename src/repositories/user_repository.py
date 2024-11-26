from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models.user import User
from src.repositories.base import BaseRepository


class UserRepository(BaseRepository):
    async def check_ip(self, ip_address: str, session: AsyncSession) -> bool:
        query = select(self.model).where(self.model.ip_address == ip_address)
        res = await session.execute(query)
        return res.scalar_one_or_none()


def get_user_repository() -> UserRepository:
    return UserRepository(model=User)
