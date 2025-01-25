from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from loguru import logger

from ..models import *
from ..core import db_manager


@db_manager
async def add_user(
    session: AsyncSession,
    tg_id: int,
    name: str,
    username: Optional[str] = None,
    language_code: Optional[str] = "ru"
):
    user = await session.scalar(select(UserOrm).filter(UserOrm.tg_id == tg_id))
    if user:
        return user
    await session.execute(insert(UserOrm).values(
        tg_id=tg_id,
        name=name,
        username=username,
        language_code=language_code
    ))
    await session.commit()
    logger.info(f"User {name} added to database")



