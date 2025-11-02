from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Any, Awaitable
from bot.database.database_settings import async_session_maker
from bot.database.blacklist_repository import BlacklistRepository
from bot.database.blacklist_service import BlacklistService

class BlacklistMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        async with async_session_maker() as session:
            repository = BlacklistRepository()
            blacklist_service = BlacklistService(repository)

            data['session'] = session
            data['blacklist_service'] = blacklist_service

            try:
                if hasattr(event, 'from_user') and event.from_user:
                    is_banned = await blacklist_service.check_ban(session, event.from_user.id)
                    if is_banned:
                        await event.answer("Вы забанены в этом боте")
                        return None

                result = await handler(event, data)
                await session.commit()
                return result
            except Exception as e:
                await session.rollback()
                raise e