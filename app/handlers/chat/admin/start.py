from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import Command


admin_start_router = Router(name=__name__)


@admin_start_router.message(Command("panel", "admin"))
async def admin_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, 'Hello, admin!')


