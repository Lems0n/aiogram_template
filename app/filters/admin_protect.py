from aiogram.types import Message
from aiogram.filters import Filter

from secure import settings



class AdminProtectFilter(Filter):
    async def __call__(self, message: Message):
        return message.from_user.id == settings.tg.admin_id
    
