from sqlalchemy import String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional

from .base import Base
from ..tools import CreateTableName



class UserOrm(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    name: Mapped[str] = mapped_column(String(64))
    username: Mapped[Optional[str]] = mapped_column(String(32))
    language_code: Mapped[Optional[str]] = mapped_column(String(2))
    

