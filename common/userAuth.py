from flask import render_template
from init import app, redis_client
from common.DataHelper import getFromRedis


def authCheck(data=None):
    if data is None:
        data = {"userId": 0, "token": ""}
    token = getFromRedis(data["userId"])
    if not token:
        return False
    elif token != data["token"]:
        return False
    else:
        return True


def checkauth(userId, token):
    def wrapper(func):
        def subwrapper(*args, **kwargs):
            print(kwargs["token"])
            temp = func(*args, **kwargs)
            return temp
        return subwrapper()
    return wrapper
