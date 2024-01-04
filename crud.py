from sqlalchemy.orm import Session
import models


def get_user_by_id(db, user_id):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_all_users(db):
    return db.query(models.User).all()


def create_user(db, user):
    db_user = models.User(username=user.username, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
