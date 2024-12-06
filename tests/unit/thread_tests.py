import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models.thread import Thread
from tests.conftest import TestModelsClass


@pytest.mark.parametrize(
    'id,status',
    [
        ('7a8b7537-c2c3-4474-a171-d1f9936beea6', 200),
        ('00000000-0000-0000-0000-000000000000', 404),
    ],
)
async def test_thread_get(id: str, status: int, async_client: AsyncClient):
    await TestModelsClass.get_entity_by_id('thread', id, status, async_client)


@pytest.mark.parametrize(
    'id,status',
    [
        ('7a8b7537-c2c3-4474-a171-d1f9936beea6', 200),
        ('00000000-0000-0000-0000-000000000000', 404),
    ],
)
async def test_thread_delete(
    id: str, status: int, async_client: AsyncClient, async_session: AsyncSession
):
    await TestModelsClass.delete_entity_by_id(
        'thread', Thread, id, status, async_client, async_session
    )


@pytest.mark.parametrize(
    'title,text,board_id,status',
    [
        ('Title', 'Text', 'c19f3243-8722-4285-89fb-9825051a5635', 200),
    ],
)
async def test_thread_create(
    title: str,
    text: str,
    board_id: str,
    status: int,
    async_client: AsyncClient,
    async_session,
):
    response = await async_client.post(
        '/thread', json={'title': title, 'text': text, 'board_id': board_id}
    )
    thread = response.json()

    if status == 200:
        await TestModelsClass.get_entity_by_id(
            'thread', thread['id'], status, async_client
        )
        await TestModelsClass.create_entity(
            response, Thread, thread['id'], status, async_session
        )
