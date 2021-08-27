from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str


class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    class Config:
        orm_mode = True

class IrisBase(BaseModel):
    sepal_length : float
    sepal_width : float
    petal_length : float
    petal_width : float

class IrisCreate(IrisBase):
    pass

class Iris(IrisBase):
    class Config:
        orm_mode = True