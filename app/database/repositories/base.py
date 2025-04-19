import abc
from typing import Generic, TypeVar, Type, Sequence

from sqlalchemy.ext.asyncio import AsyncSession


ModelType = TypeVar("ModelType") 


class AbstractRepository(abc.ABC, Generic[ModelType]):
    """Абстрактный базовый класс для репозиториев."""
    model: Type[ModelType] 

    def __init__(self, session: AsyncSession):
        self.session = session

    @abc.abstractmethod
    async def add(self, data: dict) -> ModelType:
        raise NotImplementedError

    @abc.abstractmethod
    async def get(self, **filters) -> ModelType | None:
        raise NotImplementedError

    @abc.abstractmethod
    async def get_by_id(self, obj_id: int) -> ModelType | None:
         raise NotImplementedError

    @abc.abstractmethod
    async def list(self, **filters) -> Sequence[ModelType]:
         raise NotImplementedError

    @abc.abstractmethod
    async def update(self, obj_id: int, data: dict) -> ModelType | None:
         raise NotImplementedError

    @abc.abstractmethod
    async def delete(self, **filters) -> None:
         raise NotImplementedError



