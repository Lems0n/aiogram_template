from aiogram import Dispatcher

from database import db_manager
from .throttling import ThrottlingMiddleware
from .session import DBSessionMiddleware


def setup_middlewares(dp: Dispatcher): 
    dp.message.outer_middlewaremiddleware.register(
        ThrottlingMiddleware()
    )
    dp.update.outer_middleware.register(DBSessionMiddleware(
        session_maker=db_manager.session_maker
    ))
    return dp
    