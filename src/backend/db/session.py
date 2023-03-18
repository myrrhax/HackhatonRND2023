from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import config

user = config.postgres_user.get_secret_value()
db_name = config.postgres_db.get_secret_value()
password = config.postgres_password.get_secret_value()
host = config.host.get_secret_value()

DATABASE_URL = f"postgresql+asyncpg://{user}:{password}@{host}:5432/{db_name}"

engine = create_async_engine(DATABASE_URL)
Base = declarative_base()
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def init():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
