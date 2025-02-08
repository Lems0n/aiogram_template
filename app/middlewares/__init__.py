from aiogram import Dispatcher

from .throttling import ThrottlingMiddleware
from .session import DBSessionMiddleware


def setup_middlewares(dp: Dispatcher): 
    dp.message.outer_middlewaremiddleware.register(
        ThrottlingMiddleware()
    )
    dp.update.outer_middleware.register(DBSessionMiddleware(
        session_maker=dp["session_maker"]
    ))
    return dp
    