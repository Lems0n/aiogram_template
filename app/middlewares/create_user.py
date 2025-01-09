from typing import Awaitable, Callable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import Message, User
from aiogram.dispatcher.middlewares.user_context import EventContext
from loguru import logger

from database.requests import add_user



class CreateUserMiddleware(BaseMiddleware):            
    async def __call__(self,
                       handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
                       event: Message,
                       data: Dict[str, Any]
                       ) -> Any:
        user: User = event.from_user
        try:
            info = await add_user(
                user.id, user.first_name,
                user.username, user.language_code
            )
            data["user"] = info
        except Exception as e:
            logger.error(e)
        return await handler(event, data)
        