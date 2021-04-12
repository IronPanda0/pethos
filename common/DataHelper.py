# -*- coding: utf-8 -*-
import datetime
from init import app
from itsdangerous import TimedJSONWebSignatureSerializer as TJSS

def getCurrentTime(frm="%Y-%m-%d %H:%M:%S"):
    dt = datetime.datetime.now()
    return dt.strftime(frm)

def tokenGen(user):
    t = TJSS(app.config["SECRET_KEY"],expires_in=3600)
    t.dumps(user)
    return
