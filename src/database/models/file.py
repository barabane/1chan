from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.dialects.postgresql import FLOAT, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import BaseModel


class File(BaseModel):
    __tablename__ = 'file'

    name: Mapped[str] = mapped_column(nullable=False)
    link: Mapped[str] = mapped_column(unique=True, nullable=False)
    size: Mapped[float] = mapped_column(FLOAT, nullable=False, default=0.0)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(), nullable=False, server_default=func.now()
    )
    width: Mapped[int] = mapped_column(nullable=True)
    height: Mapped[int] = mapped_column(nullable=True)

    post_id: Mapped[str] = mapped_column(ForeignKey('post.id'), nullable=False)
