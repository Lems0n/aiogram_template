from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from redis.asyncio import Redis


class TelegramSettings(BaseSettings):
    bot_token: SecretStr
    admin_id: int


class DatabaseSettings(BaseSettings):
    host: str
    port: int
    user: str
    password: SecretStr
    name: str

    def postgres_connection(self):
        return f"postgresql+asyncpg://{self.user}:{self.password.get_secret_value()}@{self.host}:{self.port}/postgres"


class RedisSettings(BaseSettings):
    host: str
    port: int
    user: str
    password: SecretStr
    db: int
    
    async def redis_connection(self) -> Redis:
        return Redis(
            host=self.host,
            port=self.port,
            username=self.user,
            password=self.password.get_secret_value(),
            db=self.db,
            decode_responses=True
        )


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=".env",
        env_file_encoding='utf-8',
        env_nested_delimiter="__"
    )
    db: DatabaseSettings
    tg: TelegramSettings
    redis: RedisSettings 
    

settings = Settings()
