from typing import List

from sqlalchemy.dialects.postgresql import ARRAY, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import BaseModel


class Board(BaseModel):
    __tablename__ = 'board'

    link: Mapped[str] = mapped_column(VARCHAR(8), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    description: Mapped[str] = mapped_column(VARCHAR(2000), nullable=True)
    tags: Mapped[List[str]] = mapped_column(ARRAY(VARCHAR), nullable=True)
