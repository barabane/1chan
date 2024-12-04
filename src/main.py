from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.routers.board_router import board_router
from src.routers.post_router import post_router
from src.routers.thread_router import thread_router
from src.routers.user_router import user_router


@asynccontextmanager
async def lifespan(_):
    yield


app = FastAPI(title='1 Chan', lifespan=lifespan)


app.include_router(board_router._router)
app.include_router(thread_router._router)
app.include_router(user_router._router)
app.include_router(post_router._router)
