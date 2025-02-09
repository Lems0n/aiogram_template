import traceback
from typing import Awaitable, Callable, Dict, Any

from aiogram import BaseMiddleware, Bot
from aiogram.types import ErrorEvent
from loguru import logger


class ErrorReportingMiddleware(BaseMiddleware):
    def __init__(self, admin_id: int):
        self.admin_id = admin_id

    async def __call__(self,
                       handler: Callable[[ErrorEvent, Dict[str, Any]], Awaitable[Any]],
                       event: ErrorEvent,
                       data: Dict[str, Any]
                       ) -> Any:
        try:
            error_message = f"Произошла ошибка: {event.exception}"

            traceback_info = traceback.format_exc()
            shortened_traceback = "\n".join(
                traceback_info.splitlines()[-5:]
            )  

            details = f"Детали:\n\n{shortened_traceback}"
            full_message = f"{error_message}\n\n{details}"

            bot: Bot = data["bot"]
            await bot.send_message(self.admin_id, full_message)
            
        except Exception as e:
            logger.error(e)

        return await handler(event, data)
    
