from typing import Any

from fastapi import status
from starlette.exceptions import HTTPException


class BaseException(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail: Any = 'Internal server error',
    ) -> None:
        super().__init__(status_code=status_code, detail=detail)


class InternalServerErrorException(BaseException):
    def __init__(self, detail: Any = 'Internal server error') -> None:
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail
        )


class BadRequestException(BaseException):
    def __init__(self, detail: Any = 'Bad request') -> None:
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)


class NotFoundException(BaseException):
    def __init__(self, detail: str = 'Not found') -> None:
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class TooManyFilesException(BadRequestException):
    def __init__(self, detail: Any = 'Слишком много файлов') -> None:
        super().__init__(detail=detail)


class FilesTotalSizeTooLarge(BadRequestException):
    def __init__(self, detail: Any = 'Общий размер файлов превышает 20 Мб') -> None:
        super().__init__(detail)
