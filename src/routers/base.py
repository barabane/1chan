import abc
from typing import Callable, List

from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.database import get_async_session
from src.dto.base import BaseDTO
from src.schemas.base import BaseCreateScheme, BaseGetScheme, BaseUpdateScheme
from src.services.base import BaseService


class BaseRouter(abc.ABC):
    def __init__(self, service: BaseService, prefix: str, tags: list[str]) -> None:
        self.service: BaseService = service
        self.prefix: str = prefix
        self.tags: List[str] = tags
        self.dto: BaseDTO = self.service.dto
        self._router = APIRouter()
        self.__define_base_routes()

    def add_route(
        self, path: str, func: Callable, methods: List[str] = ['GET'], **kwargs
    ):
        self._router.add_api_route(
            path=self.prefix + path,
            endpoint=func,
            methods=methods,
            tags=self.tags,
            **kwargs,
        )

    def delete_route(self, path: str, method: str):
        for route in self._router.routes:
            if route.path == self.prefix + path and method in route.methods:
                self._router.routes.remove(route)

    def rewrite_route(
        self,
        old_path: str,
        new_path: str,
        func: Callable,
        method: str = 'GET',
        **kwargs,
    ):
        self.delete_route(path=old_path, method=method)
        self.add_route(path=new_path, func=func, methods=[method], **kwargs)

    def __define_base_routes(self):
        get_scheme: BaseGetScheme = self.service.schemas.get_scheme
        create_scheme: BaseCreateScheme = self.service.schemas.create_scheme
        update_scheme: BaseUpdateScheme = self.service.schemas.update_scheme

        async def get_all_entities(
            session: AsyncSession = Depends(get_async_session),
        ) -> List[get_scheme]:
            return await self.service.get_all(session=session)

        async def get_entity_by_id(
            entity_id, session: AsyncSession = Depends(get_async_session)
        ) -> get_scheme:
            return await self.service.get_by_id(entity_id=entity_id, session=session)

        async def delete_entity_by_id(
            entity_id, session: AsyncSession = Depends(get_async_session)
        ):
            return await self.service.delete_by_id(entity_id=entity_id, session=session)

        async def update_entity_by_id(
            entity_id,
            entity: update_scheme,
            session: AsyncSession = Depends(get_async_session),
        ) -> get_scheme:
            return await self.service.update(
                new_entity=entity, entity_id=entity_id, session=session
            )

        async def create_entity(
            entity: create_scheme, session: AsyncSession = Depends(get_async_session)
        ) -> get_scheme:
            return await self.service.add(entity=entity, session=session)

        self.add_route(path='/all', func=get_all_entities, methods=['GET'])
        self.add_route(path='/{entity_id}', func=get_entity_by_id, methods=['GET'])
        self.add_route(
            path='/{entity_id}', func=delete_entity_by_id, methods=['DELETE']
        )
        self.add_route(path='/{entity_id}', func=update_entity_by_id, methods=['PATCH'])
        self.add_route(path='', func=create_entity, methods=['POST'])
