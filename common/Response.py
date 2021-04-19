# -*- coding: utf-8 -*-
from flask import jsonify


def ops_renderJSON(code=200, msg="操作成功~~", data={}):
    resp = {"code": code, "msg": msg, "data": data}
    return jsonify(resp)


def ops_renderIllegalJSON(msg="权限不足，请联系管理员或重新登录~~", data={}):
    return ops_renderJSON(code=403, msg=msg, data=data)


def ops_renderErrJSON(msg="系统繁忙，请稍后再试~~", data={}):
    return ops_renderJSON(code=-1, msg=msg, data=data)
