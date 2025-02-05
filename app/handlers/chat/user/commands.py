from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram_i18n import I18nContext
from sqlalchemy.ext.asyncio import AsyncSession

from database import add_user
from keyboards import inline_keyboard_builder


user_commands_router = Router(name=__name__)


@user_commands_router.message(CommandStart())
async def start(
    message: Message, 
    i18n: I18nContext, 
    session: AsyncSession
):
    user = message.from_user
    await add_user(
        session,
        user.id, user.first_name,
        user.username, user.language_code
    )
    await i18n.set_locale(user.language_code or "ru")

    mention = user.mention_html()
    return await message.reply(
        text=i18n.greeting(mention=mention),  
        reply_markup=inline_keyboard_builder()
    )


@user_commands_router.message(Command("help"))
async def help(message: Message, i18n: I18nContext):
    return message.reply(
        text=i18n.get("help"),
    )
    
    