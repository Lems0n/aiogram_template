from pydantic import SecretStr, PostgresDsn
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

    def postgres_connection(self) -> str:
        return str(
            PostgresDsn.build(
                scheme="postgresql+asyncpg",  
                username=self.user,
                password=self.password.get_secret_value(),
                host=self.host,
                port=self.port, 
                path=self.name
            )
        )


class RedisSettings(BaseSettings):
    host: str
    port: int
    user: str
    password: SecretStr
    db: int
    
    def redis_connection(self) -> Redis:
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
