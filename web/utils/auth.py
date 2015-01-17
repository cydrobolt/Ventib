from ..database import *
from hashlib import sha512
from random import choice
import string

def create_user(user, pwd):
    hashed_pwd = sha512(pwd).hexdigest()
    api_key = "".join([choice("0123456789ABCDEF") for i in range(32)])
    User.create(username=user, password=hashed_pwd, api_key=api_key)

def authenticate_user(user, pwd):
    hashed_pwd = sha512(pwd).hexdigest()
    matching = User.select().where(User.username == user, User.password == hashed_pwd)
    if not matching:
        return False
    return matching[0]
