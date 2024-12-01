from src.routers.base import BaseRouter
from src.services.base import BaseService
from src.services.post_service import get_post_service


class PostRouter(BaseRouter):
    def __init__(self, service: BaseService, prefix: str, tags: list[str]) -> None:
        super().__init__(service, prefix, tags)

        self.rewrite_route(
            old_path='', new_path='', func=self.service.add, method='POST'
        )

        self.add_route(
            path='/files/add/{post_id}', func=self.service.add_files, methods=['POST']
        )


post_router = PostRouter(service=get_post_service(), prefix='/post', tags=['Post'])
