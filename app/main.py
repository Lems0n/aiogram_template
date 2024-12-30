import asyncio
from contextlib import suppress

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import LinkPreviewOptions
from aiogram_i18n import I18nMiddleware
from aiogram_i18n.cores import FluentRuntimeCore
from loguru import logger
from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.fsm.storage.redis import RedisStorage

from handlers import setup_routers
from middlewares import setup_middlewares
from database import create_tables
from utils import set_default_commands
from secure import settings




async def main():
    await create_tables()
    
    bot = Bot(
        token=settings.bot_token.get_secret_value(),
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
            link_preview=LinkPreviewOptions(is_disabled=True)
        )
    )

    storage = RedisStorage(
        redis=await settings.redis.redis_connection(),
        key_builder=DefaultKeyBuilder(with_bot_id=True, with_destiny=True),
    )
    
    dp = Dispatcher(storage=storage)
    setup_middlewares(dp)
    setup_routers(dp)
    
    i18n_middleware = I18nMiddleware(
        core=FluentRuntimeCore(path="app/locales/{locale}")
    )
    i18n_middleware.setup(dispatcher=dp)
    
    await set_default_commands(bot)
    logger.info("Bot started")
    await dp.start_polling(bot)

     
if __name__ == "__main__":
    with suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(main())
        
    logger.info("Bot stopped")
    __import__("sys").exit(0)

