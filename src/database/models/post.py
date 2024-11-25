from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.dialects.postgresql import INTEGER, TIMESTAMP, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import BaseModel


class Post(BaseModel):
    __tablename__ = 'post'

    number: Mapped[int] = mapped_column(
        INTEGER, unique=True, autoincrement=True, nullable=False
    )
    author: Mapped[str] = mapped_column(ForeignKey('user.ip_address'), nullable=False)
    text: Mapped[str] = mapped_column(VARCHAR(15000), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(), nullable=False, server_default=func.now()
    )
