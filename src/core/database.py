from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from .config import settings

engine = create_async_engine(
    url=settings.database_url,
    pool_size=5,
    max_overflow=3,
)