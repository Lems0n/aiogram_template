from aiogram import Router

from filters import AdminProtectFilter
from .start import admin_start_router


def setup_admin_routers() -> Router:
    router = Router()
    router.message.filter(AdminProtectFilter())
    router.include_routers(
        admin_start_router
    )
    return router

