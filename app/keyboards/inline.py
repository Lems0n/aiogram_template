from aiogram_i18n.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram_i18n import LazyProxy


def get_main_keyboard(locale: str = "ru") -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(
            text=LazyProxy("profile", locale=locale),
            callback_data="profile"
        )],
        [InlineKeyboardButton(
            text=LazyProxy("settings", locale=locale),
            callback_data="settings"
        )]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


