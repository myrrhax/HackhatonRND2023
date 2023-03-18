from app_requests import AddUser
from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
import logging
import uvicorn
import json
from db.session import get_session, init
from settings import config
import asyncio
import numpy as np
import cv2
from sqlalchemy.future import select
from db.models.user import User
from db.repositories.user_repository import add_user, get_user_with_name
from db.repositories.image_repository import get_image_by_id, get_images, add_image
from db.models.user import User
from pydantic import BaseModel
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_session
from db.repositories.user_repository import add_user
from jwt_utils import sign_JWT, JWTBearer
from face_check import Recognize

app = FastAPI()
logger = logging.getLogger(__name__)

@app.on_event('startup')
async def app_startup():
    await init()

@app.post('/user/register', status_code=201)
async def register(req: AddUser,session: AsyncSession = Depends(get_session)):
    try:
        user = await add_user(req, session)
        return {'user_token': sign_JWT(user.id, user.name) }
    except Exception as e:
        return HTTPException(status_code=400)
    
@app.post('/user/login', status_code=200)
async def login(req: AddUser,session: AsyncSession = Depends(get_session)):
    user = await get_user_with_name(req.name, session)
    if req.password == user.password:
        return {'user_token': sign_JWT(user.id, user.name) }

    
    
@app.post('/image/add', dependencies=[Depends(JWTBearer())])
async def add_post(file: UploadFile, session: AsyncSession = Depends(get_session)):
    file = await file.read()
    tags_json = json.dumps([])
    try:
        await add_image(file, tags_json, session)
    except Exception:
        return HTTPException(status_code=422)

@app.post('/image/search', dependencies=[Depends(JWTBearer())])
async def add_post(file: UploadFile, session: AsyncSession = Depends(get_session)):
    file = await file.read()
    nparr = np.fromstring(file, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    images = await get_images(session)
    images_bytes = [i.image for i in images]
    Recognize(img_np, images_bytes)
    return {'msg': 'OK'}


if __name__ == '__main__':
    host = config.app_host.get_secret_value()
    port = int(config.port.get_secret_value())
    logger.info(msg=f"Trying to start application on {host}:{port}")
    uvicorn.run(app, host=host, port=port)
