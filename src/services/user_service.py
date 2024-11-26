from sqlalchemy.ext.asyncio import AsyncSession

from src.dto.base import BaseDTO
from src.dto.user_dto import get_user_dto
from src.repositories.user_repository import UserRepository, get_user_repository
from src.schemas.base import BaseSChemas
from src.schemas.user_schemas import get_user_schemas
from src.services.base import BaseService


class UserService(BaseService):
    def __init__(
        self, repository: UserRepository, schemas: BaseSChemas, dto: BaseDTO
    ) -> None:
        super().__init__(repository, schemas, dto)

    async def check_ip(self, ip_address: str, session: AsyncSession):
        user_exists = await self.repository.check_ip(
            ip_address=ip_address, session=session
        )

        if not user_exists:
            return await self.add(
                entity=self.dto.create_dto(ip_address=ip_address), session=session
            )

        return True


def get_user_service() -> UserService:
    return UserService(
        repository=get_user_repository(), schemas=get_user_schemas(), dto=get_user_dto()
    )
