from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.types import LinkPreviewOptions

from secure import settings


def create_bot() -> Bot:
    return Bot(
        token=settings.tg.bot_token.get_secret_value(),
        default=DefaultBotProperties(
            parse_mode="HTML",
            link_preview=LinkPreviewOptions(is_disabled=True)
        )
    )