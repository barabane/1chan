from src.routers.base import BaseRouter
from src.services.post_service import get_post_service


class UserRouter(BaseRouter):
    pass


user_router = UserRouter(service=get_post_service(), prefix='/user', tags=['User'])
