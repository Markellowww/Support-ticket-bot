from contextlib import suppress
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from fluent.runtime import FluentLocalization
from sqlalchemy.ext.asyncio import AsyncSession

from bot.config import config
from bot.database.blacklist_service import BlacklistService
from bot.handler.admin_handler import extract_id

router = Router()
router.message.filter(F.chat.id == config.admin_chat_id)

@router.message(Command(commands=["ban"]), F.reply_to_message)
async def cmd_ban(message: Message, l10n: FluentLocalization, blacklist_service: BlacklistService, session: AsyncSession):
    try:
        user_id = extract_id(message.reply_to_message)
    except ValueError as ex:
        return await message.reply(str(ex))

    await blacklist_service.default_ban(session, int(user_id))

    await message.reply(
        l10n.format_value(
            msg_id="user-banned",
            args={"id": user_id}
        )
    )

    return None

@router.message(Command(commands=["shadowban"]), F.reply_to_message)
async def cmd_shadowban(message: Message, l10n: FluentLocalization, blacklist_service: BlacklistService, session: AsyncSession):
    try:
        user_id = extract_id(message.reply_to_message)
    except ValueError as ex:
        return await message.reply(str(ex))

    await blacklist_service.shadow_ban(session, int(user_id))

    await message.reply(
        l10n.format_value(
            msg_id="user-shadowbanned",
            args={"id": user_id}
        )
    )
    return None

@router.message(Command(commands=["unban"]), F.reply_to_message)
async def cmd_unban(message: Message, l10n: FluentLocalization, blacklist_service: BlacklistService, session: AsyncSession):
    try:
        user_id = extract_id(message.reply_to_message)
    except ValueError as ex:
        return await message.reply(str(ex))

    with suppress(KeyError):
        await blacklist_service.unban_user(session, int(user_id))

    await message.reply(
        l10n.format_value(
            msg_id="user-unbanned",
            args={"id": user_id}
        )
    )
    return None


@router.message(Command("list_banned"))
async def cmd_list_banned(message: Message, blacklist_service: BlacklistService, l10n: FluentLocalization, session: AsyncSession):
    banned_users = await blacklist_service.get_default_banned_users(session)
    shadowbanned_users = await blacklist_service.get_shadow_banned_users(session)

    has_bans = len(banned_users) > 0 or len(shadowbanned_users) > 0

    if not has_bans:
        await message.answer(l10n.format_value("no-banned"))
        return

    result = []
    if len(banned_users) > 0:
        result.append(l10n.format_value("list-banned-title"))
        for user in banned_users:
            result.append(f"• #id{user.banned_chat_id}")

    if len(shadowbanned_users) > 0:
        result.append('\n{}'.format(l10n.format_value("list-shadowbanned-title")))
        for user in shadowbanned_users:
            result.append(f"• #id{user.banned_chat_id}")

    await message.answer("\n".join(result))