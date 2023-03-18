from db.session import Base
from sqlalchemy import Column, String, Integer

class User(Base):
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, unique=True)
    password = Column(String)

    __tablename__ = 'users'