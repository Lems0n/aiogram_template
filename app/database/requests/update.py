from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any

from ..models import *
from ..tools import db_connection
from sqlalchemy import update



@db_connection
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
    
    