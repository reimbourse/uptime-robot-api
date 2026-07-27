from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from src.core.config import settings

engine = create_async_engine(
    url=settings.database_url,
    echo=False,
    pool_pre_ping=True,
    pool_recycle=60,
    pool_size=5,
    max_overflow=3,
)

async_session_maker = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def get_async_session():
    async with async_session_maker() as session:
        yield session
