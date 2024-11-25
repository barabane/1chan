from src.routers.base import BaseRouter
from src.services.post_service import get_post_service


class PostRouter(BaseRouter):
    pass


post_router = PostRouter(service=get_post_service(), prefix='/post', tags=['Post'])
