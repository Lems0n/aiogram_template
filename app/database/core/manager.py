from typing import Any, Callable, TypeVar
from sqlalchemy.ext.asyncio import (
    create_async_engine, async_sessionmaker,
    AsyncSession, AsyncEngine
)

from secure import settings


T = TypeVar('T')


class DatabaseManager:
    def __init__(self, db_url: str, **kwargs: Any):
        self.engine: AsyncEngine = create_async_engine(
            db_url,
            **kwargs
        )
        self.session_maker: async_sessionmaker[
            AsyncSession
        ] = async_sessionmaker(
            self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autoflush=False,
        )

    async def dispose(self):
        await self.engine.dispose()

    def __call__(
        self, func: Callable[..., T]
    ) -> Callable[..., T]:
        async def wrapper(*args, **kwargs):
            async with self.session_maker() as session:
                return await func(session, *args, **kwargs)
        return wrapper


db_manager = DatabaseManager(
    settings.db.postgres_connection()
)