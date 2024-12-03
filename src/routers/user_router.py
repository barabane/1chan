from src.routers.base import BaseRouter
from src.services.user_service import get_user_service


class UserRouter(BaseRouter):
    pass


user_router = UserRouter(service=get_user_service(), prefix='/user', tags=['User'])
