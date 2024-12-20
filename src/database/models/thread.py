import uuid
from datetime import datetime

from sqlalchemy import ForeignKey, Sequence, func
from sqlalchemy.dialects.postgresql import INTEGER, TIMESTAMP, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import BaseModel


class Thread(BaseModel):
    __tablename__ = 'thread'

    number: Mapped[int] = mapped_column(
        INTEGER,
        Sequence('thread_unique_number'),
        unique=True,
        autoincrement=True,
        nullable=False,
    )
    title: Mapped[str] = mapped_column(VARCHAR(200), nullable=False)
    text: Mapped[str] = mapped_column(VARCHAR(15000), nullable=False)
    likes_count: Mapped[int] = mapped_column(INTEGER, nullable=False, default=0)
    dislikes_count: Mapped[int] = mapped_column(INTEGER, nullable=False, default=0)
    posters_count: Mapped[int] = mapped_column(INTEGER, nullable=False, default=0)
    posts_count: Mapped[int] = mapped_column(INTEGER, nullable=False, default=0)
    files_count: Mapped[int] = mapped_column(INTEGER, nullable=False, default=0)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(), nullable=False, server_default=func.now()
    )

    board_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('board.id'), nullable=False)
