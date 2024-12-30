from aiogram.filters.callback_data import CallbackData


class GoBack(CallbackData, prefix="back"):
    step: int
    
    