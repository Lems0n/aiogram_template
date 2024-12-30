from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from loguru import logger

from ..models import *
from ..tools import DatabaseConnection


connection = DatabaseConnection()


@connection
async def get_user(
    session: AsyncSession,
    user_id: int
):
    user = await session.scalar(select(UserOrm).filter(UserOrm.tg_id == user_id))
    if user:
        return user
    return None