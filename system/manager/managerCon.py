from flask import Blueprint, request, make_response, render_template, jsonify, redirect, url_for
from flask_cors import CORS
from common.DataHelper import tokenGen, storeInRedis, getFromRedis, removeFromRedis
from init import db, app
from model.user import User
from common.Response import ops_renderErrJSON, ops_renderJSON, ops_renderIllegalJSON
from common.userAuth import *

CORS(app, supports_credentials=True)

manager = Blueprint('manager', __name__, url_prefix='/manager')


@manager.route('/list', methods=['POST'])
def managerList():
    userId = request.values["userId"] if "userId" in request.values else None
    token = request.values["token"] if "token" in request.values else None
    data = {
        "userId": userId,
        "token": token
    } if userId and token is not None else None
    auth = authCheck(data)
    if not auth:
        app.logger.info("权限不足，用户id:%s的登录态无效"%userId)
        return redirect(url_for("welcome.index"))
    # else后面接权限正常情况下的代码
    else:
        if request.method == 'POST':
            res = request.values
            page = int(res['page'])
            per_page = int(res['per_page'])
            if (page == None):
                page = 1
            if (per_page == None):
                per_page = 10
            result = User.query.filter_by(authority=1).limit(per_page).offset((page - 1) * per_page)
            temp = {}
            data = []
            if result != None:
                for i in result:
                    temp["userid"] = i.userId
                    temp["username"] = i.userName
                    temp["password"] = i.passWord
                    temp["gender"] = i.gender
                    temp["age"] = i.age
                    temp["mail"] = i.mail
                    data.append(temp.copy())
                return ops_renderJSON(msg="查询成功", data=data)
            else:
                return ops_renderErrJSON(msg="暂无管理员")

    return ops_renderJSON(msg="查询成功")
