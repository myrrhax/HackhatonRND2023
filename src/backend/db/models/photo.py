from db.session import Base
from sqlalchemy import Column
from sqlalchemy import String, Integer
from sqlalchemy_imageattach.entity import Image, image_attachment


class Photo(Base):
    __tablename__ = 'photos'

    id = Column(Integer, auto_increment=True, primary_key=True, index=True)
    photo = Column()

