from pydantic import BaseModel


class AddUser(BaseModel):
    name: str
    password: str