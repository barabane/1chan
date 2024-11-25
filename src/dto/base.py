from pydantic import BaseModel


class BaseCreateDTO(BaseModel):
    pass


class BaseUpdateDTO(BaseModel):
    pass


class BaseGetDTO(BaseModel):
    pass


class BaseDTO:
    def __init__(
        self,
        create_dto: BaseCreateDTO = None,
        update_dto: BaseUpdateDTO = None,
        get_dto: BaseGetDTO = None,
    ):
        self.create_dto: BaseCreateDTO = create_dto
        self.update_dto: BaseUpdateDTO = update_dto
        self.get_dto: BaseGetDTO = get_dto


def get_base_dto() -> BaseDTO:
    return BaseDTO()
