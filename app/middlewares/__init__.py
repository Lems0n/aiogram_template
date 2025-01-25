from aiogram import Dispatcher

from .throttling import ThrottlingMiddleware
from .create_user import CreateUserMiddleware



def setup_middlewares(dp: Dispatcher): 
    dp.message.middleware.register(ThrottlingMiddleware())
    dp.message.middleware.register(CreateUserMiddleware())
    return dp
    