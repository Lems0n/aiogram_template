from typing import Awaitable, Callable, Dict, Any
from cachetools import TTLCache

from aiogram import BaseMiddleware
from aiogram.types import Update
from aiogram.dispatcher.middlewares.user_context import EventContext



class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, time_limit: int = 2) -> None:
        self.limit = TTLCache(maxsize=10_00, ttl=time_limit)
            
    async def __call__(self,
                       handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
                       event: Update,
                       data: Dict[str, Any]
                       ) -> Any:
        event_context: EventContext = data.get("event_context")
        user_id = event_context.user.id
        if user_id in self.limit:
            return
        else:
            self.limit[user_id] = None
        return await handler(event, data)
    
