from typing import List, Optional
from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str]


class UserBase(BaseModel):
    email: str
    is_active: bool = True


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    uid: str
    owner: Optional[UserBase]

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class User(UserBase):
    uid: str
    items: List[ItemBase] = []

    class Config:
        orm_mode = True