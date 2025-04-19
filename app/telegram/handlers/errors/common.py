from aiogram import Router
from aiogram.types import ErrorEvent
from aiogram_i18n.context import I18nContext
from loguru import logger


common_errors_router = Router(name=__name__)


@common_errors_router.error()
async def handle_all_errors(event: ErrorEvent, i18n: I18nContext):
    update = event.update
    
    if update.message:
        await update.message.answer(text=i18n.get("error"))
        
    elif update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.message.answer(text=i18n.get("error"))
    
    logger.error(f"Common Error: {event.exception}")
    
    