from db.session import Base
from sqlalchemy import Column, Text, Integer, String, LargeBinary

class Image(Base):
    __tablename__ = "images"

    image_id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    path = Column(String)
    tags = Column(String)