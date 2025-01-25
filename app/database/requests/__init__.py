from .add import add_user
from .delete import delete_user
from .get import get_user
from .update import update_user
from ..models import Base, UserOrm
from ..core import db_manager

__all__ = [
    "add_user",
    "delete_user",
    "get_user",
    "update_user",
    "create_tables",
    "drop_tables",
    "UserOrm",
    "Base"
]

async def create_tables():
    async with db_manager.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
        
async def drop_tables():
    async with db_manager.engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        