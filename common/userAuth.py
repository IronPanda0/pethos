from flask import render_template

from common.Response import ops_renderIllegalJSON, ops_renderErrJSON
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


def authRes(req):
    userId = req.headers.environ['HTTP_USERID'] if 'HTTP_USERID' in req.headers.environ else None
    token = req.headers.environ['HTTP_AUTHORIZATION'] if 'HTTP_AUTHORIZATION' in req.headers.environ else None
    data = {
        "userId": userId,
        "token": token
    } if userId and token is not None else None
    auth = authCheck(data)
    if not auth:
        app.logger.info("权限不足，用户id:%s的登录态无效"%userId)
        return ops_renderErrJSON(data={"domain":app.config["DOMAIN"]["www"]})
    else:
        return None

