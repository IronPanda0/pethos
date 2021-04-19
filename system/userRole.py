from flask import Blueprint, request, make_response, render_template, jsonify
from flask_cors import CORS
from sqlalchemy import text
import json
from common.Response import ops_renderErrJSON, ops_renderJSON
from model.userRole import Userrole

userRole = Blueprint('userRoleModule', __name__, url_prefix='/userRole')


@userRole.route("/add", methods=['GET', 'POST'])
def addUserRole():
    from init import db
    if request.method == 'GET':
        return "增加角色.html"
    if request.method == 'POST':
        res = request.values
        userName = res['userName']
        role = res['role']
        content = res['content']
        duty = res['duty']
        process = res['process']

        userRoleD = Userrole.query.filter_by(userName=userName, role=role).first()
        if (userRoleD):
            return ops_renderErrJSON(msg="该用户已有此角色，请换一个试试")

        model_userRole = Userrole()
        model_userRole.userName = userName
        model_userRole.role = role
        model_userRole.content = content
        model_userRole.process = process
        model_userRole.duty = duty

        db.session.add(model_userRole)
        db.session.commit()
        temp = {}
        temp['userName'] = userName
        temp['role'] = role
        temp['content'] = content
        temp['process'] = process
        temp['duty'] = duty
        data = []
        data.append(temp)
        return ops_renderJSON(msg="添加成功", data=data)
    return "添加成功"


@userRole.route("/update", methods=['POST'])
def updateUserRole():
    from init import db
    if request.method == 'POST':
        res = request.values
        userName = res['userName']
        role = res['role']
        content = res['content']
        duty = res['duty']
        process = res['process']
        userRoleD = Userrole.query.filter_by(userName=userName, role=role).first()
        if (userRoleD):
            return ops_renderErrJSON(msg="该用户已有此角色，请换一个试试")
        model_userRole = Userrole()
        model_userRole.userName = userName
        model_userRole.role = role
        model_userRole.content = content
        model_userRole.process = process
        model_userRole.duty = duty

        db.session.add(model_userRole)
        db.session.commit()
        temp = {}
        temp['userName'] = userName
        temp['role'] = role
        temp['content'] = content
        temp['process'] = process
        temp['duty'] = duty
        data = []
        data.append(temp)
        return ops_renderJSON(msg="修改成功", data=data)
    return "修改成功"


@userRole.route("/list", methods=['POST'])
def listUserRoles():
    if request.method == 'POST':
        res = request.values
        page = int(res['page'])
        per_page = int(res['per_page'])
        userName = res['userName']
        if (page == None):
            page = 1
        if (per_page == None):
            per_page = 10
        if (len(userName) == 0):
            result = Userrole.query.limit(per_page).offset((page - 1) * per_page)
        else:
            result = Userrole.query.filter_by(userName=userName).limit(per_page).offset((page - 1) * per_page)
        temp = {}
        data = []
        if (result != None):
            for i in result:
                temp['userRoleId'] = i.userRoleId
                temp['userName'] = i.userName
                temp['role'] = i.role
                temp['content'] = i.content
                temp['process'] = i.process
                temp['duty'] = i.duty
                data.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=data)
        else:
            return ops_renderErrJSON(msg="查询失败，目前没有角色")


@userRole.route("/delete", methods=['POST'])
def deleteUserRole():
    from init import db
    if request.method == 'POST':
        res = request.values
        userName = res['userName']
        role = res['role']
        # diseaseNameD = db.session.query(Disease).filter(Disease.diseaseName == diseaseName).first()
        userRoleD = db.session.query(Userrole).filter(Userrole.userName == userName, Userrole.role == role).first()
        if userRoleD == None:
            return ops_renderErrJSON(msg="目前没有该角色，请重新确认")

        temp = {}
        temp['userName'] = userName
        temp['role'] = role
        data = []
        data.append(temp)

        db.session.delete(userRoleD)
        db.session.commit()

        return ops_renderJSON(msg="删除成功", data=data)
