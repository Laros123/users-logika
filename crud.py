

def get_user_by_id(db, user_id):
    for user in db:
        if user['id'] == user_id:
            return user
    return None


def get_all_users(db):
    return db


def create_user(db, user):
    if db:
        user_id = db[-1]['id']+1
    else:
        user_id = 1
    db.append({'id': user_id, 'username': user.username, 'email': user.email})
