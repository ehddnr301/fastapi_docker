from sqlalchemy.orm import Session

from . import models, schemas


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def get_iris(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Iris).offset(skip).limit(limit).all()

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def create_iris(db: Session, iris: schemas.IrisCreate):
    db_iris = models.Iris(**iris.dict())
    db.add(db_iris)
    db.commit()
    db.refresh(db_iris)
    return db_iris
