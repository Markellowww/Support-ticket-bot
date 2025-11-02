import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()

def get_database_url():
    url = os.getenv("DATABASE_URL", "")
    if not url:
        return "postgresql+asyncpg://bot_user_ex:bot_password_ex@postgres_service:5432/support_db_ex"

    if url.startswith("postgresql://"):
        url = url.replace("postgresql://", "postgresql+asyncpg://", 1)
    elif not url.startswith("postgresql+asyncpg://"):
        url = f"postgresql+asyncpg://{url}"

    return url

database_url = get_database_url()

engine = create_async_engine(
    database_url,
    echo=True,
    pool_pre_ping=True,
    pool_recycle=300,
)

async_session_maker = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_db_session():
    async with async_session_maker() as session:
        try:
            yield session
        finally:
            await session.close()

async def close_db():
    await engine.dispose()