import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models.user import User
from tests.conftest import TestModelsClass


@pytest.mark.parametrize(
    'id,status',
    [
        ('cee389d8-dc88-44e6-9d10-6e796e1aeccf', 200),
        ('00000000-0000-0000-0000-000000000000', 404),
    ],
)
async def test_user_get(id: str, status: int, async_client: AsyncClient):
    await TestModelsClass.get_entity_by_id('user', id, status, async_client)


@pytest.mark.parametrize(
    'id,status',
    [
        ('cee389d8-dc88-44e6-9d10-6e796e1aeccf', 200),
        ('00000000-0000-0000-0000-000000000000', 404),
    ],
)
async def test_user_delete(
    id: str, status: int, async_client: AsyncClient, async_session: AsyncSession
):
    await TestModelsClass.delete_entity_by_id(
        'user', User, id, status, async_client, async_session
    )


@pytest.mark.parametrize(
    'email,ip_address,status',
    [
        ('test@test.ru', '255.255.255.255', 200),
        ('test1@test.ru', '192.192.192.192', 200),
        ('', '193.193.193.193', 200),
    ],
)
async def test_user_create(
    email: str,
    ip_address: str,
    status: int,
    async_client: AsyncClient,
    async_session: AsyncSession,
):
    response = await async_client.post(
        '/user', json={'email': email, 'ip_address': ip_address}
    )
    user = response.json()

    assert status == response.status_code

    if status == 200:
        await TestModelsClass.get_entity_by_id('user', user['id'], status, async_client)
        await TestModelsClass.create_entity(
            response, User, user['id'], status, async_session
        )
