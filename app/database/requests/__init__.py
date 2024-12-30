from .add import add_user
from .delete import delete_user
from .get import get_user
from .update import update_user
from ..models import Base, engine, UserOrm



async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
        
async def drop_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        