from flask import Blueprint, request, make_response, render_template, jsonify
from flask_cors import CORS
from sqlalchemy import text
import json
from init import db
from model.case import Case
from model.medicine import Medicine
from model.casemedicine import Casemedicine
from common.Response import ops_renderErrJSON, ops_renderJSON

case = Blueprint('caseModule', __name__, url_prefix='/case')


@case.route("/add", methods=['GET', 'POST'])
def addCase():
    # html文件修改为新建题目的文件
    if request.method == "POST":
        req = request.values
        # 暂时略过合法性检测
        caseName = req['caseName']
        animalName = req['animalName']
        diseaseName = req['diseaseName']
        caseInfo = req['caseInfo']
        videoUrl = req['videoUrl']
        imageUrl = req['imageUrl']
        processUrl1 = req['processUrl1']
        processUrl2 = req['processUrl2']
        processUrl3 = req['processUrl3']
        caseNameD = Case.query.filter_by(caseName=caseName).first()
        if caseNameD:
            return ops_renderErrJSON(msg="相同题干已存在，请再换一个试试")
        # 注册写入数据库
        model_case = Case()
        model_case.caseName = caseName
        model_case.caseName = caseName
        model_case.caseInfo = caseInfo
        model_case.diseaseName = diseaseName
        model_case.animalName = animalName
        model_case.videoUrl = videoUrl
        model_case.imageUrl = imageUrl
        db.session.add(model_case)
        db.session.commit()
        # json化data
        temp = {}
        temp["caseName"] = caseName
        temp["caseName"] = caseName
        temp["caseInfo"] = caseInfo
        temp["diseaseName"] = diseaseName
        temp["animalName"] = animalName
        temp["videoUrl"] = videoUrl
        temp["imageUrl"] = imageUrl
        temp["processUrl1"] = processUrl1
        temp["processUrl2"] = processUrl2
        temp["processUrl3"] = processUrl3
        data = []
        data.append(temp)
        return ops_renderJSON(msg="添加成功", data=data)
    return "添加成功"


@case.route("/list", methods=['POST'])
def listCase():
    if request.method == 'POST':
        res = request.values
        page = res['page']
        per_page = res['per_page']
        diseaseName = res['diseaseName']
        if (page == ''):
            page = 1
        else:
            page = int(page)
        if (per_page == ''):
            per_page = 10
        else:
            per_page = int(per_page)
        if (diseaseName == "all"):
            result = Case.query.limit(per_page).offset((page - 1) * per_page)
        else:
            result = Case.query.filter_by(diseaseName=diseaseName).limit(per_page).offset((page - 1) * per_page)
        temp = {}
        data = []
        if (result != None):
            for i in result:
                temp["caseName"] = i.caseName
                temp["caseName"] = i.caseName
                temp["caseInfo"] = i.caseInfo
                temp["diseaseName"] = i.diseaseName
                temp["animalName"] = i.animalName
                temp["videoUrl"] = i.videoUrl
                temp["imageUrl"] = i.imageUrl
                temp["processUrl1"] = i.processUrl1
                temp["processUrl2"] = i.processUrl2
                temp["processUrl3"] = i.processUrl3
                data.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=data)
        else:
            return ops_renderErrJSON(msg="查询失败，目前没有分类")


# 根据caseName删除病例
@case.route("/delete", methods=['POST'])
def deletecase():
    from init import db
    if request.method == 'POST':
        res = request.values
        caseName = res['caseName']
        caseNameD = db.session.query(Case).filter(Case.caseName == caseName).first()
        if caseNameD == None:
            return ops_renderErrJSON(msg="目前没有该病例，请再次确认")
        caseInfo = caseNameD.caseInfo
        diseaseName = caseNameD.diseaseName
        animalName = caseNameD.animalName
        videoUrl = caseNameD.videoUrl
        imageUrl = caseNameD.imageUrl
        processUrl1 = caseNameD.processUrl1
        processUrl2 = caseNameD.processUrl2
        processUrl3 = caseNameD.processUrl3
        temp = {}
        temp["caseName"] = caseName
        temp["caseInfo"] = caseInfo
        temp["diseaseName"] = diseaseName
        temp["animalName"] = animalName
        temp["videoUrl"] = videoUrl
        temp["imageUrl"] = imageUrl
        temp["processUrl1"] = processUrl1
        temp["processUrl2"] = processUrl2
        temp["processUrl3"] = processUrl3
        data = []
        data.append(temp)

        db.session.delete(caseNameD)
        db.session.commit()

        return ops_renderJSON(msg="删除成功", data=data)


@case.route("/addCaseMedicine", methods=['POST'])
def addCaseMedicine():
    from init import db
    if request.method == 'POST':
        res = request.values
        caseId = res['caseId']
        medicineName = res['medicineName']
        medicineD = db.session.query(Medicine).filter_by(name=medicineName).first()
        if medicineD == None:
            return ops_renderErrJSON(msg="没有这种药品，请确认后再添加")
        else:
            curMedicineId = medicineD.medicineId
            model_caseMedicine = Casemedicine()
            model_caseMedicine.medicineId = curMedicineId
            model_caseMedicine.caseId = caseId
            db.session.add(model_caseMedicine)
            db.session.commit()
        temp = {}
        temp["caseId"] = caseId
        temp["medicineName"] = medicineName
        data = []
        data.append(temp)
        return ops_renderJSON(msg="病例添加药品成功", data=data)
