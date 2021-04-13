# -*- coding: utf-8 -*-
import datetime
from init import app, redis_client
from itsdangerous import TimedJSONWebSignatureSerializer as TJSS
import time


def getCurrentTime(frm="%Y-%m-%d %H:%M:%S"):
    dt = datetime.datetime.now()
    return dt.strftime(frm)


def tokenGen(user):
    t = TJSS(app.config["SECRET_KEY"], expires_in=3600)
    token = t.dumps(user)
    token = token.decode()
    return token


def storeInRedis(itemId=0, data="", expire=60):
    redisId = str(itemId).encode('utf-8')
    data = str(data).encode('utf-8')
    expires = int(time.time()) + expire
    data_key = "dyn_data/%s" % redisId
    p = redis_client.pipeline()
    # data_key是键，data是值
    p.set(data_key, data)
    p.expireat(data_key, expires)
    p.execute()


def getFromRedis(itemId=0):
    user_id = str(itemId).encode('utf-8')
    data_key = "dyn_data/%s" % user_id
    data = redis_client.get(data_key)
    if data:
        return data.decode()
    return None
