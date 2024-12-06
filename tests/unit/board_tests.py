from typing import List

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models.board import Board
from tests.conftest import TestModelsClass


@pytest.mark.parametrize(
    'id,status',
    [
        ('f1bd03af-8d6c-40ad-a820-54b7f4a97cf5', 200),
        ('00000000-0000-0000-0000-000000000000', 404),
    ],
)
async def test_board_get(id: str, status: int, async_client: AsyncClient):
    await TestModelsClass.get_entity_by_id('board', id, status, async_client)


@pytest.mark.parametrize(
    'id,status',
    [
        ('f1bd03af-8d6c-40ad-a820-54b7f4a97cf5', 200),
        ('00000000-0000-0000-0000-000000000000', 404),
    ],
)
async def test_board_delete(
    id: str, status: int, async_client: AsyncClient, async_session: AsyncSession
):
    await TestModelsClass.delete_entity_by_id(
        'board', Board, id, status, async_client, async_session
    )


@pytest.mark.parametrize(
    'link,name,description,tags,status',
    [
        ('/test/', 'test', 'test', ['#test'], 200),
        ('/test0/', 'test0', 'test0', [], 200),
        ('/test1/', 'test1', 'test1', None, 422),
        ('/test2/', 'test2', 'test2', [''], 422),
    ],
)
async def test_board_create(
    link: str,
    name: str,
    description: str,
    tags: List[str],
    status: int,
    async_client: AsyncClient,
    async_session: AsyncSession,
):
    response = await async_client.post(
        '/board',
        json={'link': link, 'name': name, 'description': description, 'tags': tags},
    )
    board = response.json()

    if status == 200:
        await TestModelsClass.get_entity_by_id(
            'board', board['id'], status, async_client
        )
        await TestModelsClass.create_entity(
            response, Board, board['id'], status, async_session
        )
