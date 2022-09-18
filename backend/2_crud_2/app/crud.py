import models, schemas

def get_user(user_id: str):
    user = models.User.nodes.first(uid=user_id)
    if not user is None:
        return user.to_json()
    else:
        return None

def get_user_by_email(email: str):
    user = models.User.nodes.get_or_none(email=email)
    if not user is None:
        return user.to_json()
    else:
        return None

def get_users(skip: int = 0, limit: int = 100):
    users = models.User.nodes.all()[skip:limit]
    if not len(users) == 0:
        return [user.to_json() for user in users]
    else:
        return None

def create_user(user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(
        email=user.email,
        hashed_password=fake_hashed_password, is_active=True).save()
    db_user.refresh()
    return db_user.to_json()

def get_items(skip: int = 0, limit: int = 100):
    return [item.to_json() for item in models.Item.nodes.all()[skip:limit]]

def create_user_item(item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict()).save()
    user = models.User.nodes.first(uid=user_id)
    db_item.owner.connect(user)
    
    db_item.save()
    db_item.refresh()
    return db_item.to_json()


