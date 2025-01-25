from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update

from ..models import *
from ..core import db_manager


@db_manager
async def update_user(
    session: AsyncSession,
    user_id: int,
    field: str,
    value: Any
):
    await session.execute(
        update(UserOrm)
        .filter(UserOrm.tg_id == user_id)
        .values({field: value})
    )
    await session.commit()
    
    