from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import *
from ..core import db_manager


@db_manager
async def delete_user(
    session: AsyncSession,
    user_id: int
):
    await session.execute(delete(UserOrm).filter(UserOrm.tg_id == user_id))
    await session.commit()
    
    