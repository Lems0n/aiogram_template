from aiogram import Dispatcher

from .chat import setup_chat_routers
from .errors import setup_errors_routers


def setup_routers(dp: Dispatcher):
    dp.include_routers(
        setup_chat_routers(),
        setup_errors_routers(),
    )
    return dp
