from aiogram import Dispatcher

from .throttling import ThrottlingMiddleware
from .session import DBSessionMiddleware


def setup_middlewares(dp: Dispatcher): 
    dp.message.middleware(ThrottlingMiddleware())
    dp.update.middleware(
        DBSessionMiddleware(dp["session_maker"])
    )
    return dp
    