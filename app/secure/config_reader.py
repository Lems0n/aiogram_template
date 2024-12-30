from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from aioredis import Redis as AsyncIORedis



class PostgreSQLSettings(BaseSettings):
    host: str
    port: int
    user: str
    password: SecretStr
    db: str
    
    def postgres_connection(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password.get_secret_value()}@{self.host}:{self.port}/{self.db}"


class RedisSettings(BaseSettings):
    host: str
    port: int
    user: str
    password: SecretStr
    db: int
    
    async def redis_connection(self) -> AsyncIORedis:
        return await AsyncIORedis.from_url(
            f'redis://{self.user}:{self.password.get_secret_value()}@{self.host}:{self.port}/{self.db}',
            decode_responses=True
        )


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=".env",
        env_file_encoding="utf-8"
    )
    bot_token: SecretStr
    admin_id: int
    
    database: PostgreSQLSettings = PostgreSQLSettings(_env_prefix="PSQL_")
    redis: RedisSettings = RedisSettings(_env_prefix="REDIS_")


settings = Settings()
