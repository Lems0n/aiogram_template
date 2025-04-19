from typing import Optional
from database import AbstractUnitOfWork, UserOrm


class UserService:
    def __init__(self, uow: AbstractUnitOfWork):
        self._uow = uow

    async def register_user(
        self, 
        user_id: int, 
        name: str,
        username: Optional[str] = None, 
        language_code: Optional[str] = "ru"
    ) -> UserOrm:
        """Регистрирует или обновляет пользователя."""
        async with self._uow: 
            user = await self._uow.users.get(tg_id=user_id)
            user_data = {
                "tg_id": user_id,
                "name": name,
                "username": username,
                "language_code":  language_code
            }
            if user:
                updated_user = await self._uow.users.update(user_id, user_data)
                if updated_user is None:
                     raise Exception("Couldn't update the user") 
                user = updated_user
            else:
                user = await self._uow.users.add(user_data)
        return user 

    async def get_user(self, user_id: int) -> UserOrm | None:
        """Получает пользователя по ID."""
        async with self._uow: 
            user = await self._uow.users.get_by_id(user_id)
            return user 