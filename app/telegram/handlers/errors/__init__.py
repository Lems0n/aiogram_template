from aiogram import Router

from .common import common_errors_router
from .orm import orm_errors_router
from .telegram import telegram_errors_router


def setup_errors_routers() -> Router:
    router = Router()
    router.include_routers(
        telegram_errors_router,
        orm_errors_router,
        common_errors_router,
    )
    return router
