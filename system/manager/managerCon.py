from flask import Blueprint, request, make_response, render_template, jsonify, redirect, url_for
from flask_cors import CORS
from common.DataHelper import tokenGen, storeInRedis, getFromRedis, removeFromRedis
from init import db, app
from model.user import User
from common.Response import ops_renderErrJSON, ops_renderJSON, ops_renderIllegalJSON
from common.userAuth import *

CORS(app, supports_credentials=True)

manager = Blueprint('manager', __name__, url_prefix='/manager')

@manager.route('/userlist', methods=['POST'])
def userList():
    userId = request.values["userId"] if "userId" in request.values else None
    token = request.values["token"] if "token" in request.values else None
    data = {
        "userId": userId,
        "token": token
    } if userId and token is not None else None
    auth = authCheck(data)
    if not auth:
        app.logger.info("权限不足，用户id:%s的登录态无效"%userId)
        return ops_renderIllegalJSON()
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
            result = User.query.filter_by(authority=2).limit(per_page).offset((page - 1) * per_page)
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
                return ops_renderErrJSON(msg="暂无用户")

    return ops_renderJSON(msg="查询成功")

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
        return ops_renderIllegalJSON()
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

@manager.route('/delete', methods=['POST'])
def deleteUser():
    userId = request.values["userId"] if "userId" in request.values else None
    token = request.values["token"] if "token" in request.values else None
    data = {
        "userId": userId,
        "token": token
    } if userId and token is not None else None
    auth = authCheck(data)
    if not auth:
        app.logger.info("权限不足，用户id:%s的登录态无效"%userId)
        return ops_renderIllegalJSON()
    # else后面接权限正常情况下的代码
    else:
        if request.method == 'POST':
            res = request.values
            username = res['username']
            delNameD = User.query.filter_by(userName = username)
            if delNameD is None:
                return ops_renderErrJSON(msg="该用户不存在或已被删除！")

            db.session.delete(delNameD)
            db.session.commit()
            return ops_renderJSON(msg="删除成功")

@manager.route('/changepwd', methods=['POST'])
def changepwd():
    userId = request.values["userId"] if "userId" in request.values else None
    token = request.values["token"] if "token" in request.values else None
    data = {
        "userId": userId,
        "token": token
    } if userId and token is not None else None
    auth = authCheck(data)
    # auth = True
    if not auth:
        app.logger.info("权限不足，用户id:%s的登录态无效"%userId)
        return ops_renderIllegalJSON()
    # else后面接权限正常情况下的代码
    else:
        if request.method == 'POST':
            res = request.values
            username = res['username']
            oldpwd = res['password']
            newpwd = res['new_password']
            checknewpwd = res['new_password_verify']
            if username is None or len(username) < 1:
                return ops_renderErrJSON(msg="目标用户不存在！")
            if newpwd is None or len(newpwd) < 6:
                return ops_renderErrJSON(msg="请输入正确的新密码，并且不能小于6个字符~~")
            if checknewpwd != newpwd:
                return ops_renderErrJSON(msg="两次密码不一致，请检查无误再操作~~")
            changepwdD = db.session.query(User).filter_by(userName = username).first()
            if changepwdD is None:
                return ops_renderErrJSON(msg="该用户不存在或已被删除！")
            if changepwdD.passWord != oldpwd:
                return ops_renderErrJSON(msg="旧密码错误！")

            changepwdD.passWord = newpwd
            db.session.commit()
            return ops_renderJSON(msg="密码修改成功！")


@manager.route('/changeinfo', methods=['POST'])
def changeinfo():
    userId = request.values["userId"] if "userId" in request.values else None
    token = request.values["token"] if "token" in request.values else None
    data = {
        "userId": userId,
        "token": token
    } if userId and token is not None else None
    auth = authCheck(data)
    # auth = True
    if not auth:
        app.logger.info("权限不足，用户id:%s的登录态无效"%userId)
        return ops_renderIllegalJSON()
    # else后面接权限正常情况下的代码
    else:
        if request.method == 'POST':
            res = request.values
            username = res['username']
            gender = 1 if res['gender'] == 'girl' else 2
            age = res['age']
            email = res['email']
            if username is None or len(username) < 1:
                return ops_renderErrJSON(msg="目标用户不存在！")
            changeinfoD = db.session.query(User).filter_by(userName = username).first()
            if changeinfoD is None:
                return ops_renderErrJSON(msg="该用户不存在或已被删除！")

            changeinfoD.gender = gender
            changeinfoD.age = age
            changeinfoD.mail = email
            db.session.commit()
            return ops_renderJSON(msg="信息修改成功！")