from datetime import datetime

from sqlalchemy import ForeignKey, Sequence, func
from sqlalchemy.dialects.postgresql import INTEGER, TIMESTAMP, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import BaseModel


class Post(BaseModel):
    __tablename__ = 'post'

    number: Mapped[int] = mapped_column(
        INTEGER,
        Sequence('post_unique_number'),
        unique=True,
        autoincrement=True,
        nullable=False,
    )
    text: Mapped[str] = mapped_column(VARCHAR(15000), nullable=False)
    user_id: Mapped[str] = mapped_column(ForeignKey('user.id'), nullable=False)
    thread_id: Mapped[str] = mapped_column(ForeignKey('thread.id'), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(), nullable=False, server_default=func.now()
    )
