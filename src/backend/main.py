from app_requests import Register, Login, UpdateTags
from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
import logging
import uvicorn
import json
import shutil
from db.session import get_session, init
from settings import config
import asyncio
import numpy as np
import cv2
from sqlalchemy.future import select
from db.models.user import User
from db.repositories.user_repository import add_user, get_user_with_name
from db.repositories.image_repository import get_image_by_id, get_images, add_image, update_image
from db.models.user import User
from pydantic import BaseModel
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_session
from db.repositories.user_repository import add_user
from jwt_utils import sign_JWT, JWTBearer
from face_check import recognize
import os
import PIL.Image as Image
import uuid
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

origins = [
    'http://localhost:8080'
]

IMAGE_DIR = 'media/'
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

logger = logging.getLogger(__name__)

@app.on_event('startup')
async def app_startup():
    await init()

@app.post('/user/register', status_code=201)
async def register(req: Register,session: AsyncSession = Depends(get_session)):
    try:
        user = await add_user(req, session)
        return {'token': sign_JWT(user.user_id, user.name) }
    except Exception as e:
        return HTTPException(status_code=400)
    
@app.post('/user/login', status_code=200)
async def login(req: Login,session: AsyncSession = Depends(get_session)):
    user = await get_user_with_name(req.name, session)
    if req.password == user.password:
        return {'token': sign_JWT(user.user_id, user.name) }

    
    
@app.post('/image/add', dependencies=[Depends(JWTBearer())])
async def add_post(file: UploadFile, session: AsyncSession = Depends(get_session)):
    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()
    with open(f'{IMAGE_DIR}{file.filename}', 'wb') as f:
        f.write(contents)
    tags_json = json.dumps([])
    result = await add_image(f'{IMAGE_DIR}{file.filename}', tags_json, session)
    return {'id': result.image_id}
    
@app.post('/image/search', dependencies=[Depends(JWTBearer())])
async def add_post(file: UploadFile, session: AsyncSession = Depends(get_session)):
    file.filename = f"{uuid.uuid4()}.jpg"
    path_to_file = f'{IMAGE_DIR}{file.filename}'
    contents = await file.read()
    with open(path_to_file, 'wb') as f:
        f.write(contents)
        cv2.resize(f, (300, 200), interpolation=cv2.INTER_LINEAR)

    images = await get_images(session)
    images_pathes = [i[0].path for i in images]
    result = recognize(path_to_file, images_pathes)
    if result is None:
        await add_image(path_to_file, json.dumps([]), session)
        raise HTTPException(status_code=404)
    else:
        os.remove(path_to_file)
        return {'msg': result}
    
@app.get('/image/{id}', response_class=FileResponse)
async def get_image(id: int, session: AsyncSession = Depends(get_session)):
    image = await get_image_by_id(id, session)
    if image is None:
        raise HTTPException(status_code=404)
    
    return image[0].path

@app.patch('/image')
async def update_tags(req: UpdateTags, session: AsyncSession = Depends(get_session)):
    image = await get_image_by_id(req.id, session)
    if image is None:
        raise HTTPException(status_code=404)
    
    result = await update_image(req.id, req.tags, session)
    tags = json.loads(result.tags)
    return {'id': result.image_id, 'tags': tags}


if __name__ == '__main__':
    host = config.app_host.get_secret_value()
    port = int(config.port.get_secret_value())
    logger.info(msg=f"Trying to start application on {host}:{port}")
    uvicorn.run(app, host=host, port=port)
