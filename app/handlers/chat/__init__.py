from aiogram import Router

from .user import setup_user_routers
from .admin import setup_admin_routers


def setup_chat_routers() -> Router:
    router = Router(name=__name__)
    router.include_routers(
        setup_user_routers(),
        setup_admin_routers()
    )
    return router
