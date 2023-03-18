from db.session import Base
from sqlalchemy import Column, Text, Integer, String, LargeBinary

class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    image = Column(LargeBinary)
    tags = Column(String)