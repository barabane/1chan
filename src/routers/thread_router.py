from src.routers.base import BaseRouter
from src.services.thread_service import ThreadService, get_thread_service


class ThreadRouter(BaseRouter):
    def __init__(self, service: ThreadService, prefix: str, tags: list[str]) -> None:
        super().__init__(service, prefix, tags)

        self.add_route(path='/thread/top', func=self.service.get_top_threads)

        self.add_route(
            path='/thread/local/top/{board_id}', func=self.service.get_local_top
        )

        self.add_route(path='/thread/{thread_id}/like', func=self.service.like_thread)

        self.add_route(
            path='/thread/{thread_id}/dislike', func=self.service.dislike_thread
        )


thread_router = ThreadRouter(
    service=get_thread_service(), prefix='/thread', tags=['Thread']
)
