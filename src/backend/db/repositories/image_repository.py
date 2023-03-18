import json
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from db.models.image import Image
from sqlalchemy.future import select
from sqlalchemy import update

async def add_image(path, tags_json: str, session: AsyncSession) -> Image:
    image = Image(path=path, tags=tags_json)
    session.add(image)
    await session.commit()
    return image

async def get_image_by_id(id: int, session: AsyncSession) -> Image:
    query = select(Image).where(Image.image_id == id)
    result= await session.execute(query)
    return result.first()

async def get_images(session: AsyncSession):
    query = select(Image)
    result = await session.execute(query)
    return result

async def update_image(image_id: int, tags: List[str], session: AsyncSession) -> Image:
    query = update(Image)\
                    .returning(Image.image_id, Image.tags)\
                    .where(Image.image_id == image_id)\
                    .values(tags=json.dumps(tags))
    result = await session.execute(query)
    await session.commit()
    return result.first()