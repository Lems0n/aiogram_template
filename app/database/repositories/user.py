from typing import Sequence
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from .base import AbstractRepository
from ..models import UserOrm


class UserRepository(AbstractRepository[UserOrm]):
    model = UserOrm

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def add(self, data: dict) -> UserOrm:
        user = self.model(**data)
        self.session.add(user)
        return user

    async def get(self, **filters) -> UserOrm | None:
        stmt = select(self.model).filter_by(**filters)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_by_id(self, obj_id: int) -> UserOrm | None:
        return await self.session.scalar(select(self.model).where(self.model.tg_id == obj_id))

    async def list(self, **filters) -> Sequence[UserOrm]:
        stmt = select(self.model).filter_by(**filters)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def update(self, obj_id: int, data: dict) -> UserOrm | None:
        user = await self.get_by_id(obj_id)
        if user:
            for key, value in data.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            await self.session.flush([user])
            return user
        return None 

    async def delete(self, **filters) -> None:
        stmt = delete(self.model).filter_by(**filters)
        await self.session.execute(stmt)

