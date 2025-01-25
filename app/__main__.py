import asyncio
from contextlib import suppress

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import LinkPreviewOptions
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram_i18n import I18nMiddleware
from aiogram_i18n.cores import FluentRuntimeCore
from loguru import logger

from handlers import setup_routers
from middlewares import setup_middlewares
from database import create_tables, db_manager
from utils import set_default_commands
from secure import settings


async def on_startup(bot: Bot):
    await create_tables()
    await set_default_commands(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    logger.info("Bot started")


async def on_shutdown():
    await db_manager.dispose()
    logger.info("Bot stopped")


async def main():
    bot = Bot(
        token=settings.tg.bot_token.get_secret_value(),
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
    
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    i18n_middleware = I18nMiddleware(
        core=FluentRuntimeCore(path="app/locales/{locale}")
    )
    i18n_middleware.setup(dispatcher=dp)
    
    await dp.start_polling(
        bot,
        allowed_updates=dp.resolve_used_update_types()
    )

     
if __name__ == "__main__":
    with suppress(KeyboardInterrupt):
        asyncio.run(main())
        
    __import__("sys").exit(0)

