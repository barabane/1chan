from sqlalchemy.dialects.postgresql import VARCHAR
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import BaseModel


class User(BaseModel):
    __tablename__ = 'user'

    email: Mapped[str] = mapped_column(VARCHAR(50), unique=True, nullable=True)
    ip_address: Mapped[str] = mapped_column(VARCHAR(50), unique=True, nullable=True)
