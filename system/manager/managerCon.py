from flask import Blueprint, request, make_response, render_template, jsonify, redirect, url_for
from flask_cors import CORS
from common.DataHelper import tokenGen, storeInRedis, getFromRedis, removeFromRedis
from init import db, app
from model.user import User
from common.Response import ops_renderErrJSON, ops_renderJSON, ops_renderIllegalJSON

CORS(app, supports_credentials=True)

manager = Blueprint('manager', __name__, url_prefix='/manager')


@manager.route('/list', methods=['POST'])
def managerList():
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
