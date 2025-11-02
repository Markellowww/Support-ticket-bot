import asyncio
import logging

from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.client.telegram import TelegramAPIServer
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
from bot.handler import setup_routers
from fluent.runtime import FluentLocalization, FluentResourceLoader
from bot.util.commands import set_bot_commands
from bot.middleware import L10nMiddleware
from pathlib import Path

from bot.config import config

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    locales_dir = Path(__file__).parent.joinpath("locale")
    l10n_loader = FluentResourceLoader(str(locales_dir) + "/{locale}")
    l10n = FluentLocalization(["ru"], ["strings.ftl", "errors.ftl"], l10n_loader)

    bot = Bot(token=config.bot_token.get_secret_value())
    router = setup_routers()

    dispatcher = Dispatcher()
    dispatcher.include_router(router)

    if config.custom_bot_api:
        bot.session.api = TelegramAPIServer.from_base(config.custom_bot_api, is_local=True)

    dispatcher.update.middleware(L10nMiddleware(l10n))

    await set_bot_commands(bot)

    try:
        if not config.webhook_domain:
            await bot.delete_webhook()
            await dispatcher.start_polling(bot, allowed_updates=dispatcher.resolve_used_update_types())
        else:
            # Webhook setup (Optional)
            aiohttp_logger = logging.getLogger("aiohttp.access")
            aiohttp_logger.setLevel(logging.CRITICAL)

            await bot.set_webhook(
                url=config.webhook_domain + config.webhook_path,
                drop_pending_updates=True,
                allowed_updates=dispatcher.resolve_used_update_types()
            )

            app = web.Application()
            SimpleRequestHandler(dispatcher=dispatcher, bot=bot).register(app, path=config.webhook_path)
            runner = web.AppRunner(app)
            await runner.setup()
            site = web.TCPSite(runner, host=config.app_host, port=config.app_port)
            await site.start()

            await asyncio.Event().wait()
    finally:
        await bot.session.close()

asyncio.run(main())
