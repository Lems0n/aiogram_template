from aiogram.types import Message
from aiogram.filters import Filter



class DataLengthFilter(Filter):
    def __init__(self, data_length: int) -> None:
        self.length = data_length

    async def __call__(self, message: Message) -> bool:
        if message.text:
            return len(message.text) <= self.length
        else:
            return True # Другие типы сообщений (фото, видео, аудио) будут также проходить
        
        