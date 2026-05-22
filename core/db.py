from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from core.config import settings

# 1. Ensure your settings.DATABASE_URL starts with an async driver prefix!
# Example: "postgresql+asyncpg://..." instead of "postgresql://..."
# Example: "sqlite+aiosqlite:///./db.sqlite" instead of "sqlite:///./db.sqlite"
engine = create_async_engine(
    settings.DATABASE_URL,
    future=True,
    echo=True  # Optional: logs raw SQL queries to your console for easy debugging
)

# 2. Use async_sessionmaker instead of sessionmaker
SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False  # Crucial for async so objects stay readable after commit
)

# 3. Rewrite your generator function using async/await
async def get_db():
    async with SessionLocal() as db:
        try:
            yield db
        finally:
            await db.close()
