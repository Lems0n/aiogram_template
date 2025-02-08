from aiogram import Dispatcher

from secure import settings
from .reporting import ErrorReportingMiddleware
from .throttling import ThrottlingMiddleware
from .session import DBSessionMiddleware


def setup_middlewares(dp: Dispatcher): 
    dp.error.middleware(
        ErrorReportingMiddleware(settings.tg.admin_id)
    )
    dp.message.middleware(ThrottlingMiddleware())
    dp.update.middleware(
        DBSessionMiddleware(dp["session_maker"])
    )
    return dp
    