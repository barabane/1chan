import asyncio

import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import settings
from src.database.database import async_session_maker, engine
from src.database.models.base import BaseModel
from src.database.models.board import Board
from src.database.models.thread import Thread
from src.database.models.user import User
from src.main import app


@pytest_asyncio.fixture(scope='session', autouse=True)
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope='session', autouse=True)
async def prepare_database():
    assert settings.MODE == 'TEST'

    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)
        await conn.run_sync(BaseModel.metadata.create_all)

        await conn.execute(
            insert(User).values(
                {
                    'id': 'cee389d8-dc88-44e6-9d10-6e796e1aeccf',
                    'ip_address': '192.192.192.192',
                    'email': None,
                }
            )
        )

        await conn.execute(
            insert(Board).values(
                [
                    {
                        'id': 'f1bd03af-8d6c-40ad-a820-54b7f4a97cf5',
                        'link': '/main/',
                        'name': 'Main',
                        'description': 'main',
                        'tags': ['#main'],
                    },
                    {
                        'id': 'c19f3243-8722-4285-89fb-9825051a5635',
                        'link': '/news/',
                        'name': 'News',
                        'description': 'news',
                        'tags': ['#news'],
                    },
                ]
            )
        )

        await conn.execute(
            insert(Thread).values(
                {
                    'id': '7a8b7537-c2c3-4474-a171-d1f9936beea6',
                    'number': 1,
                    'title': 'Title',
                    'text': 'Teeeeext',
                    'board_id': 'c19f3243-8722-4285-89fb-9825051a5635',
                }
            )
        )


@pytest_asyncio.fixture(scope='session')
async def async_session():
    async with async_session_maker() as session:
        yield session


@pytest_asyncio.fixture(scope='session')
async def async_client():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url='http://test'
    ) as client:
        yield client


class TestModelsClass:
    @staticmethod
    async def get_entity_by_id(
        model_name: str, id, status: int, async_client: AsyncClient
    ):
        response = await async_client.get(f'/{model_name}/{id}')

        assert status == response.status_code

    @staticmethod
    async def delete_entity_by_id(
        model_name: str,
        model,
        id,
        status: int,
        async_client: AsyncClient,
        async_session: AsyncSession,
    ):
        response = await async_client.delete(f'/{model_name}/{id}')

        assert status == response.status_code

        entity = await async_session.get(model, id)
        assert entity is None

    @staticmethod
    async def create_entity(
        response, model, id, status: int, async_session: AsyncSession
    ):
        assert status == response.status_code

        entity = await async_session.get(model, id)
        assert entity

        if status == 200:
            entity = response.json()
            entity_from_db = await async_session.get(model, entity['id'])

        assert entity_from_db
