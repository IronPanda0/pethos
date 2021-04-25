from flask import Blueprint, request, make_response, render_template, jsonify
from flask_cors import CORS
from sqlalchemy import text
import json
from init import db
from model.hospital import Hospital
from model.case import Case
from common.Response import ops_renderErrJSON, ops_renderJSON
import decimal

hospital = Blueprint('hospitalModule', __name__, url_prefix='/hospital')

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder


# decimal不能json化
class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        super(JSONEncoder, self).default(o)


class Flask(_Flask):
    json_encoder = JSONEncoder


@hospital.route("/add", methods=['GET', 'POST'])
def addHospital():
    # html文件修改为新建题目的文件
    if request.method == "POST":
        req = request.values
        # 暂时略过合法性检测
        caseName = req['caseName']
        day = req['day']
        pay = req['pay']
        caseNameD = db.session.query(Case).filter_by(caseName=caseName).first()
        if caseNameD == None:
            return ops_renderErrJSON(msg="目前没有该病例，请确认")
        # 注册写入数据库
        hospitalD = db.session.query(Hospital).filter_by(caseName=caseName).first()
        if hospitalD != None:
            return ops_renderErrJSON(msg="目前已有该病例的住院记录")
        model_hospital = Hospital()
        model_hospital.caseName = caseName
        model_hospital.day = day
        model_hospital.pay = pay
        db.session.add(model_hospital)
        db.session.flush()
        db.session.commit()
        # json化data
        temp = {}
        temp["caseName"] = caseName
        temp["pay"] = pay
        temp["day"] = day
        temp["hospitalId"] = model_hospital.hospitalId
        data = []
        data.append(temp)
        return ops_renderJSON(msg="添加病例成功", data=data)


@hospital.route("/list", methods=['POST'])
def listHospital():
    if request.method == 'POST':
        res = request.values
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
        result = db.session.query(Hospital).limit(per_page).offset((page - 1) * per_page)
        temp = {}
        data = []
        if (result != None):
            for i in result:
                temp["caseName"] = i.caseName
                temp["pay"] = i.pay
                temp["day"] = i.day
                temp["hospitalId"] = i.hospitalId
                data.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=data)
        else:
            return ops_renderErrJSON(msg="查询失败，目前没有住院")


@hospital.route("/update", methods=['POST'])
def updatehospital():
    from init import db
    if request.method == 'POST':
        req = request.values
        hospitalId = req['hospitalId']
        caseName = req['caseName']
        day = req['day']
        pay = req['pay']
        caseNameD = db.session.query(Hospital).filter_by(caseName=caseName).first()
        if caseNameD:
            return ops_renderErrJSON(msg="相同住院记录已经存在，请换一个再试试。")
        else:
            hospitalU = db.session.query(Hospital).filter_by(hospitalId=hospitalId).first()

            hospitalU.caseName = caseName
            hospitalU.day = day
            hospitalU.pay = pay
            db.session.commit()

            # json化data
            temp = {}
            temp["caseName"] = caseName
            temp["pay"] = pay
            temp["day"] = day
            temp["hospitalId"] = hospitalId
            data = []
            data.append(temp)
            return ops_renderJSON(msg="修改住院成功", data=data)


# 根据hospitalId删除住院
@hospital.route("/delete", methods=['POST'])
def deletehospital():
    from init import db
    if request.method == 'POST':
        res = request.values
        hospitalId = res['hospitalId']
        hospitalD = db.session.query(Hospital).filter_by(hospitalId=hospitalId).first()
        if hospitalD == None:
            return ops_renderErrJSON(msg="目前没有该住院记录，请再次确认")
        else:

            temp = {}
            temp["caseName"] = hospitalD.caseName
            temp["pay"] = hospitalD.pay
            temp["day"] = hospitalD.day
            temp["hospitalId"] = hospitalD.hospitalId
            data = []
            data.append(temp)
            db.session.delete(hospitalD)
            db.session.commit()

            return ops_renderJSON(msg="删除住院成功", data=data)
