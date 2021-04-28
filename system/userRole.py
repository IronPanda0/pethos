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
        userRoleId = res['userRoleId']
        userName = res['userName']
        role = res['role']
        content = res['content']
        duty = res['duty']
        process = res['process']
        userRoleD = db.session.query(Userrole).filter_by(userName=userName, role=role).first()
        if userRoleD:
            return ops_renderErrJSON(msg="该用户已有此角色，请换一个试试")
        else:
            userRoleU = db.session.query(Userrole).filter_by(userRoleId=userRoleId).first()
            if userRoleU != None:
                userRoleU.userName = userName
                userRoleU.role = role
                userRoleU.content = content
                userRoleU.process = process
                userRoleU.duty = duty
                db.session.commit()
                temp = {}
                temp['userName'] = userName
                temp['role'] = role
                temp['content'] = content
                temp['process'] = process
                temp['duty'] = duty
                data = []
                data.append(temp)
                return ops_renderJSON(msg="用户角色修改成功", data=data)
            else:
                return ops_renderErrJSON(msg="不存在这个用户，无法修改")


@userRole.route("/list", methods=['POST'])
def listUserRoles():
    if request.method == 'POST':
        res = request.values
        userName = res['userName']
        page = res['page']
        per_page = res['per_page']
        if (page == ''):
            page = 1
        else:
            page = int(page)
        if (per_page == ''):
            per_page = 10
        else:
            per_page = int(per_page)
        if (len(userName) == 0):
            result = Userrole.query.limit(per_page).offset((page - 1) * per_page)
        else:
            result = Userrole.query.filter_by(userName=userName).limit(per_page).offset((page - 1) * per_page)
        temp = {}
        data = []
        if (result.count() != 0):
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
            return ops_renderErrJSON(msg="查询失败，目前该用户没有角色")


@userRole.route("/delete", methods=['POST'])
def deleteUserRole():
    from init import db
    if request.method == 'POST':
        res = request.values
        userRoleId = res['userRoleId']
        # diseaseNameD = db.session.query(Disease).filter(Disease.diseaseName == diseaseName).first()
        userRoleD = db.session.query(Userrole).filter_by(userRoleId=userRoleId).first()
        if userRoleD == None:
            return ops_renderErrJSON(msg="目前没有该角色，请重新确认")
        temp = {}
        temp['userName'] = userRoleD.userName
        temp['role'] = userRoleD.role
        temp['duty'] = userRoleD.duty
        temp['process'] = userRoleD.process
        data = []
        data.append(temp)

        db.session.delete(userRoleD)
        db.session.commit()

        return ops_renderJSON(msg="删除成功", data=data)
