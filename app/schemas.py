from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    title: str

    class Config:
        orm_mode = True