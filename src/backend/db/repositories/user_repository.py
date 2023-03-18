from sqlalchemy.ext.asyncio import AsyncSession
from db.models.user import User
from sqlalchemy.future import select
from app_requests import Register

async def get_user_by_id(id: int, session: AsyncSession) -> User:
    query = select(User).where(User.user_id == id)
    result= await session.execute(query)
    return result.first()[0]

async def add_user(user: Register, session: AsyncSession):
    user = User(name=user.name, password=user.password)
    session.add(user)
    await session.commit()
    return user

async def get_user_with_name(name: str, session: AsyncSession):
    query = select(User).where(User.name == name)
    result = await session.execute(query)
    return result.first()[0]
