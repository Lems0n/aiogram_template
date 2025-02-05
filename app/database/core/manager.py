from typing import Any

from sqlalchemy.ext.asyncio import (
    create_async_engine, async_sessionmaker,
    AsyncSession, AsyncEngine
)
from loguru import logger

from secure import settings


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
        logger.info('Database connection closed')


db_manager = DatabaseManager(
    settings.db.postgres_connection()
)