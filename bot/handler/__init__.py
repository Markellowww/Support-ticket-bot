from aiogram import Router

def setup_routers() -> Router:
    from . import unsupported_reply, admin_no_reply, bans, admin_handler, message_edit, user_handler

    router = Router()
    router.include_router(unsupported_reply.router)
    router.include_router(bans.router)
    router.include_router(admin_no_reply.router)
    router.include_router(admin_handler.router)
    router.include_router(message_edit.router)
    router.include_router(user_handler.router)

    return router