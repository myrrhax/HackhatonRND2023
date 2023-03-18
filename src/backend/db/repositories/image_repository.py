from sqlalchemy.ext.asyncio import AsyncSession
from db.models.image import Image
from sqlalchemy.future import select

async def add_image(bytes, tags_json: str, session: AsyncSession) -> Image:
    image = Image(image=bytes, tags=tags_json)
    session.add(image)
    await session.commit()
    return image

async def get_image_by_id(id: int, session: AsyncSession) -> Image:
    query = select(Image).where(Image.id == id)
    result= await session.execute(query)
    return result.first()[0]

async def get_images(session: AsyncSession):
    query = select(Image)
    result = await session.execute(query)
    return result