from aiogram import Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram_i18n import I18nMiddleware
from aiogram_i18n.cores import FluentRuntimeCore

from telegram import setup_routers, setup_middlewares
from database import db_manager
from secure import settings


def create_dispatcher() -> Dispatcher:
    storage = RedisStorage(
        redis=settings.redis.redis_connection(),
        key_builder=DefaultKeyBuilder(with_bot_id=True, with_destiny=True),
    )
    dp = Dispatcher(
        storage=storage,
        session_pool=db_manager.session_maker
    )
    
    setup_middlewares(dp)
    setup_routers(dp)

    i18n_middleware = I18nMiddleware(
        core=FluentRuntimeCore(path="app/locales/{locale}")
    )
    i18n_middleware.setup(dp)
    return dp
