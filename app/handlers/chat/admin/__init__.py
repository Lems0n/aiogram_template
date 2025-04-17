from aiogram import Router

from filters import AdminProtectFilter
from .commands import admin_commands_router
from .callbacks import admin_callbacks_router
from .messages import admin_messages_router


def setup_admin_routers() -> Router:
    router = Router()
    router.message.filter(AdminProtectFilter())
    router.include_routers(
        admin_commands_router,
        admin_callbacks_router,
        admin_messages_router   
    )
    return router

