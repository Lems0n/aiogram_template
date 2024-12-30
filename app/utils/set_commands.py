from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats



async def set_default_commands(bot: Bot):
    commands = [
        BotCommand(command='start', description='Запустить бота'),
        BotCommand(command='help', description='Инструкция по использованию'),
    ]
    await bot.set_my_commands(
        commands, scope=BotCommandScopeAllPrivateChats()
    )
    
    