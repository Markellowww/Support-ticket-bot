from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User
from fluent.runtime import FluentLocalization, FluentResourceLoader
from pathlib import Path

class LocalizationMiddleware(BaseMiddleware):
    def __init__(self):
        locales_dir = Path(__file__).parent.parent / "locale"
        loader = FluentResourceLoader(str(locales_dir) + "/{locale}")

        self.localizations = {
            "ru": FluentLocalization(["ru"], ["strings.ftl", "errors.ftl"], loader),
            "en": FluentLocalization(["en"], ["strings.ftl", "errors.ftl"], loader),
        }
        self.default_l10n = self.localizations["ru"]

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        user: User = data.get("event_from_user")

        if user and user.language_code in self.localizations:
            l10n = self.localizations[user.language_code]
        else:
            l10n = self.default_l10n

        data["l10n"] = l10n
        return await handler(event, data)