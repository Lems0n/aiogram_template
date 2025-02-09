from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import *


async def get_user(
    session: AsyncSession,
    user_id: int
):
    user = await session.scalar(select(UserOrm).filter(UserOrm.tg_id == user_id))
    return user 
