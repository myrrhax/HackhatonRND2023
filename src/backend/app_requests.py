from pydantic import BaseModel
from typing import List

class Register(BaseModel):
    name: str
    password: str

class Login(BaseModel):
    name: str 
    password: str
 
class UpdateTags(BaseModel):
    id: int
    tags: List[str]
