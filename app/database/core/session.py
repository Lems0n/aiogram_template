from sqlalchemy.ext.asyncio import async_sessionmaker
from .engine import engine



async_session = async_sessionmaker(
    engine,
    autoflush=False,
    expire_on_commit=False
)
