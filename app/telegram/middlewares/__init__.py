from aiogram import Dispatcher
from aiogram.utils.callback_answer import CallbackAnswerMiddleware

from secure import settings
from .reporting import ErrorReportingMiddleware
from .throttling import ThrottlingMiddleware
from .db import DBMiddleware


def setup_middlewares(dp: Dispatcher): 
    dp.callback_query.middleware(CallbackAnswerMiddleware())
    dp.error.middleware(
        ErrorReportingMiddleware(settings.tg.admin_id)
    )
    dp.message.middleware(ThrottlingMiddleware())
    dp.update.middleware(
        DBMiddleware(dp["session_pool"])
    )
    return dp
    