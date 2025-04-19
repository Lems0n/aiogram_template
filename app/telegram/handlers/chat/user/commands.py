from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram_i18n import I18nContext

from services import UserService
from keyboards import inline_keyboard_builder


user_commands_router = Router(name=__name__)


@user_commands_router.message(CommandStart())
async def start(
    message: Message, 
    i18n: I18nContext, 
    user_service: UserService
):
    user = message.from_user
    await user_service.register_user(
        user.id, user.first_name,
        user.username, user.language_code
    )
    await i18n.set_locale(user.language_code or "ru")

    mention = user.mention_html()
    return await message.reply(
        text=i18n.greeting(mention=mention),  
        reply_markup=inline_keyboard_builder(
            "Click me",
            "on_click_data",
            locale=i18n.get_current().locale   
        )
    )


@user_commands_router.message(Command("help"))
async def help(message: Message, i18n: I18nContext):
    return message.reply(
        text=i18n.get("help"),
    )
    
    