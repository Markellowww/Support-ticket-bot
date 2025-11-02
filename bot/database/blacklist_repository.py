from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from .blacklist import Blacklist
from typing import Sequence

class BlacklistRepository:
    async def add_to_blacklist(self, session: AsyncSession, banned_chat_id: int, selected_type: str = 'default') -> Blacklist:
        blacklist_entry = Blacklist(
            banned_chat_id=banned_chat_id,
            type=selected_type
        )
        session.add(blacklist_entry)
        await session.commit()
        await session.refresh(blacklist_entry)
        return blacklist_entry

    async def remove_from_blacklist(self, session: AsyncSession, banned_chat_id: int) -> bool:
        result = await session.execute(
            delete(Blacklist).where(Blacklist.banned_chat_id == banned_chat_id)
        )
        await session.commit()
        return result.rowcount > 0

    async def is_banned(self, session: AsyncSession, chat_id: int) -> bool:
        result = await session.execute(
            select(Blacklist).where(Blacklist.banned_chat_id == chat_id)
        )
        return result.scalar_one_or_none() is not None

    async def get_all_banned(self, session: AsyncSession) -> Sequence[Blacklist]:
        result = await session.execute(
            select(Blacklist).order_by(Blacklist.date.desc())
        )
        return result.scalars().all()

    async def update_ban_type(self, session: AsyncSession, chat_id: int, new_type: str) -> Blacklist:
        result = await session.execute(
            update(Blacklist)
            .where(Blacklist.banned_chat_id == chat_id)
            .values(type=new_type)
            .returning(Blacklist)
        )
        await session.commit()
        return result.scalar_one_or_none()

    async def get_default_banned_users(self, session: AsyncSession) -> Sequence[Blacklist]:
        result = await session.execute(
            select(Blacklist)
            .where(Blacklist.type == 'default')
            .order_by(Blacklist.date.desc())
        )
        return result.scalars().all()

    async def get_shadow_banned_users(self, session: AsyncSession) -> Sequence[Blacklist]:
        result = await session.execute(
            select(Blacklist)
            .where(Blacklist.type == 'shadow')
            .order_by(Blacklist.date.desc())
        )
        return result.scalars().all()