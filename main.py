from fastapi import FastAPI
import crud
import schemas


app = FastAPI()

users = []


@app.get('/users/{user_id}')
def get_user(user_id: int):
    return crud.get_user_by_id(users, user_id)


@app.get('/users')
def get_users():
    return crud.get_all_users(users)


@app.post('/create_user')
def create_user(user: schemas.User):
    crud.create_user(users, user)
