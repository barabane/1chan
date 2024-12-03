from fastapi import Request
from sqlalchemy import select

from src.database.database import async_session_maker
from src.database.models.user import User
from src.dto.user_dto import UserCreateDTO
from src.routers.user_router import user_router


async def get_current_user(request: Request):
    async with async_session_maker() as session:
        user = await session.execute(
            select(User).where(User.ip_address == request.client.host)
        )
        user = user.scalar_one_or_none()

        if user:
            return user
        else:
            user = await user_router.service.add(
                entity=UserCreateDTO(ip_address=request.client.host), session=session
            )
            await session.commit()
            return user


current_user = get_current_user
