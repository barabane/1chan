from src.dto.base import (
    BaseCreateDTO,
    BaseDTO,
    BaseGetDTO,
    BaseUpdateDTO,
)
from src.schemas.post_schemas import PostCreateScheme, PostGetScheme, PostUpdateScheme


class PostCreateDTO(BaseCreateDTO, PostCreateScheme):
    pass


class PostUpdateDTO(BaseUpdateDTO, PostUpdateScheme):
    pass


class PostGetDTO(BaseGetDTO, PostGetScheme):
    pass


class PostDTO(BaseDTO):
    def __init__(
        self,
        create_dto: PostCreateDTO = None,
        update_dto: PostUpdateDTO = None,
        get_dto: PostGetDTO = None,
    ):
        super().__init__(
            create_dto=create_dto,
            update_dto=update_dto,
            get_dto=get_dto,
        )


def get_post_dto() -> PostDTO:
    return PostDTO(
        create_dto=PostCreateDTO,
        update_dto=PostUpdateDTO,
        get_dto=PostGetDTO,
    )
