# - *- coding: utf- 8 - *-
from typing import Optional

import aiohttp


# In handler
# session = await arSession.get_session()
# response = await session.get(...)
# response = await session.post(...)

# Асинхронная сессия для запросов
class AsyncRequestSession:
    def __init__(self) -> None:
        self._session: Optional[aiohttp.ClientSession] = None

    # Получение сессии
    async def get_session(self) -> aiohttp.ClientSession:
        if self._session is None:
            new_session = aiohttp.ClientSession()
            self._session = new_session

        return self._session

    # Закрытие сессии
    async def close(self) -> None:
        if self._session is None:
            return None

        await self._session.close()
