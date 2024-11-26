from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, Request
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.database import get_async_session
from src.routers.board_router import board_router
from src.routers.post_router import post_router
from src.routers.thread_router import thread_router
from src.routers.user_router import user_router
from src.services.user_service import UserService, get_user_service


@asynccontextmanager
async def lifespan(_):
    yield


app = FastAPI(title='1 Chan', lifespan=lifespan)


@app.get('/check_ip')
async def check_ip(
    request: Request,
    user_service: UserService = Depends(get_user_service),
    session: AsyncSession = Depends(get_async_session),
):
    user = await user_service.check_ip(ip_address=request.client.host, session=session)
    return user


app.include_router(board_router._router)
app.include_router(thread_router._router)
app.include_router(user_router._router)
app.include_router(post_router._router)
