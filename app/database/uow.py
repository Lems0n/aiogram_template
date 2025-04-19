import abc
from typing import Self 

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from .repositories import UserRepository


class AbstractUnitOfWork(abc.ABC):
    users: UserRepository

    @abc.abstractmethod
    async def __aenter__(self) -> Self: 
        raise NotImplementedError

    @abc.abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError

    @abc.abstractmethod
    async def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    async def rollback(self):
        raise NotImplementedError


class UnitOfWork(AbstractUnitOfWork):
    def __init__(
        self, 
        session_factory: async_sessionmaker[AsyncSession]
    ):
        self._session_factory = session_factory
        self._session: AsyncSession | None = None 

    async def __aenter__(self) -> Self:
        self._session = self._session_factory()
        self.users = UserRepository(self._session)
        return self 

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._session:
            if exc_type:
                await self.rollback()
            else: 
                try:
                    await self.commit()
                except Exception: 
                    await self.rollback()
                    raise 
            await self._session.close()
            self._session = None 

    async def commit(self):
        if self._session:
            await self._session.commit()

    async def rollback(self):
        if self._session:
            await self._session.rollback()