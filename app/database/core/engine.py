from sqlalchemy.ext.asyncio import create_async_engine
from secure import settings


engine = create_async_engine(
    settings.db.postgres_connection(),
)

