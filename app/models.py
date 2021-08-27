from pydantic.main import BaseModel
from sqlalchemy import Boolean, Column, Float, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True, default='test')

class Iris(Base):
    __tablename__ = 'iris'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sepal_length = Column(Float, index=True)
    sepal_width = Column(Float, index=True)
    petal_length = Column(Float, index=True)
    petal_width = Column(Float, index=True)