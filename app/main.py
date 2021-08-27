from logging import error
from typing import Optional, List

from fastapi import FastAPI, Depends

from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB

import numpy as np



models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# model

iris = load_iris()
X = iris.data
y = iris.target

clf = GaussianNB()
clf.fit(X,y)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/item", response_model=schemas.Item)
def create_item_for_user(
    item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_item(db=db, item=item)

@app.get("/items", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

# predict에 쓰일 iris데이터 추가하기
@app.post('/iris', response_model=schemas.Iris)
def add_single_data(
    iris: schemas.IrisCreate, db: Session = Depends(get_db)
):
    return crud.create_iris(db, iris=iris)

# predict 결과 받기
@app.get('/iris')
def get_predict(db:Session = Depends(get_db)):
    global clf, iris
    test = crud.get_iris(db)

    item = [{
        'sepal_length': t.sepal_length,
        'sepal_width': t.sepal_width,
        'petal_length': t.petal_length,
        'petal_width': t.petal_width
    } for t in test]

    test_set = np.array([list(i.values()) for i in item])

    pred_list = clf.predict(test_set)
    result = {f'item{idx}': iris.target_names[p] for idx,p in enumerate(pred_list)}
    
    return result