from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



main_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Профиль", callback_data="profile")],
    [InlineKeyboardButton(text="Помощь", callback_data="help")],
])


