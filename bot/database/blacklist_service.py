from sqlalchemy.ext.asyncio import AsyncSession
from .blacklist_repository import BlacklistRepository
from typing import Sequence
from .blacklist import Blacklist

class BlacklistService:
    def __init__(self, blacklist_repository: BlacklistRepository):
        self.repository = blacklist_repository

    async def ban_user(self, session: AsyncSession, chat_id: int, ban_type: str = 'default') -> Blacklist:
        existing = await self.repository.is_banned(session, chat_id)
        if existing:
            return await self.repository.update_ban_type(session, chat_id, ban_type)
        return await self.repository.add_to_blacklist(session, chat_id, ban_type)

    async def default_ban(self, session: AsyncSession, chat_id: int) -> Blacklist:
        return await self.ban_user(session, chat_id, 'default')

    async def shadow_ban(self, session: AsyncSession, chat_id: int) -> Blacklist:
        return await self.ban_user(session, chat_id, 'shadow')

    async def unban_user(self, session: AsyncSession, chat_id: int) -> bool:
        return await self.repository.remove_from_blacklist(session, chat_id)

    async def get_blacklist(self, session: AsyncSession) -> Sequence[Blacklist]:
        return await self.repository.get_all_banned(session)

    async def check_ban(self, session: AsyncSession, chat_id: int) -> bool:
        return await self.repository.is_banned(session, chat_id)

    async def get_default_banned_users(self, session: AsyncSession) -> Sequence[Blacklist]:
        return await self.repository.get_default_banned_users(session)

    async def get_shadow_banned_users(self, session: AsyncSession) -> Sequence[Blacklist]:
        return await self.repository.get_shadow_banned_users(session)