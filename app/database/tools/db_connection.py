from typing import Callable, TypeVar, Generic
from ..core import async_session


T = TypeVar('T')


class DatabaseConnection(Generic[T]):
    def __init__(self):
        self._async_session = async_session

    def __call__(self, func: Callable[..., T]) -> Callable[..., T]:
        async def wrapper(*args, **kwargs):
            async with self._async_session() as session:
                return await func(session, *args, **kwargs)
        return wrapper

