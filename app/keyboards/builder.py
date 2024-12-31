from typing import Union

from aiogram_i18n import LazyProxy
from aiogram_i18n.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from .callback_factory import GoBack


def inline_keyboard_builder(
    buttons: Union[str, list[str]], 
    callback: Union[str, list[str]],
    locale: str = "ru",
):
    builder = InlineKeyboardBuilder()
    
    buttons = [buttons] if isinstance(buttons, str) else buttons
    callback = [callback] if isinstance(callback, str) else callback

    for text, data in zip(buttons, callback):
        builder.button(text=text, callback_data=data)

    builder.add(
        InlineKeyboardButton(
            text=LazyProxy("back", locale=locale), callback_data=GoBack(step=1).pack()
        )
    )
    return builder.adjust(2).as_markup()



