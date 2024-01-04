from fastapi import FastAPI, Depends
from database import LocalSession, engine
from sqlalchemy.orm import Session
import crud
import schemas
import models


models.Base.metadata.create_all(bind=engine)
app = FastAPI()

users = []


def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()


@app.get('/users/{user_id}')
def get_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_by_id(db, user_id)


@app.get('/users')
def get_users(db: Session = Depends(get_db)):
    return crud.get_all_users(db)


@app.post('/create_user')
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    crud.create_user(db, user)
