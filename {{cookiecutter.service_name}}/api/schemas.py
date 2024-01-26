from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str


class User(BaseModel):
    id: int
    username: str
    email: str
