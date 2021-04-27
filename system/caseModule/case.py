import decimal

from flask import Blueprint, request, make_response, render_template, jsonify
from flask_cors import CORS
from sqlalchemy import text
import json

from common.userAuth import authRes
from init import db
from model.animal import Animal
from model.case import Case
from model.animal import Animal
from model.medicine import Medicine
from model.fee import Fee
from model.hospital import Hospital
from model.disease import Disease
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
        info1 = req['info1']
        info2 = req['info2']
        info3 = req['info3']
        caseNameD = Case.query.filter_by(caseName=caseName).first()
        animalD = Animal.query.filter_by(animalName = animalName).first()
        if caseNameD:
            return ops_renderErrJSON(msg="相同病例已存在，请再换一个试试")
        diseaseNameD = Disease.query.filter_by(diseaseName=diseaseName).first()
        if diseaseNameD is None:
            return ops_renderErrJSON(msg="目前没有该病种，请换一个试试")
        if animalD is None:
            return ops_renderErrJSON(msg="不存在该宠物")
        # 注册写入数据库
        model_case = Case()
        model_case.caseName = caseName
        model_case.caseInfo = caseInfo
        model_case.diseaseName = diseaseName
        model_case.animalName = animalName
        model_case.videoUrl = videoUrl
        model_case.imageUrl = imageUrl
        model_case.processUrl1 = processUrl1
        model_case.processUrl2 = processUrl2
        model_case.processUrl3 = processUrl3
        model_case.info1 = info1
        model_case.info2 = info2
        model_case.info3 = info3
        model_case.animalId = animalD.animalId
        db.session.add(model_case)
        db.session.commit()
        # json化data
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
        temp["info1"] = info1
        temp["info2"] = info2
        temp["info3"] = info3
        temp["animalId"] = animalD.animalId

        data = []
        data.append(temp)
        return ops_renderJSON(msg="添加成功", data=data)


@case.route("/update", methods=['POST'])
def updateCase():
    # html文件修改为新建题目的文件
    if request.method == "POST":
        req = request.values
        # 暂时略过合法性检测
        caseId = req['caseId']
        caseName = req['caseName']
        animalName = req['animalName']
        diseaseName = req['diseaseName']
        caseInfo = req['caseInfo']
        videoUrl = req['videoUrl']
        imageUrl = req['imageUrl']
        processUrl1 = req['processUrl1']
        processUrl2 = req['processUrl2']
        processUrl3 = req['processUrl3']
        info1 = req['info1']
        info2 = req['info2']
        info3 = req['info3']
        medicineCount = req['medicineCount']
        caseU = db.session.query(Case).filter_by(caseId=caseId).first()
        oldName = caseU.caseName
        caseNameD = Case.query.filter_by(caseName=caseName).first()
        if caseNameD:
            return ops_renderErrJSON(msg="相同题干已存在，请再换一个试试")
        diseaseNameD = Disease.query.filter_by(diseaseName=diseaseName).first()
        animalNameD = Animal.query.filter_by(animalName=animalName).first()
        if animalNameD == None:
            return ops_renderErrJSON(msg="目前没有该宠物，请换一个试试")
        if diseaseNameD == None:
            return ops_renderErrJSON(msg="目前没有该病种，请换一个试试")
        # 写入数据库
        resultFee = db.session.query(Fee).filter_by(caseName=oldName).all()
        for i in resultFee:
            i.caseName = caseName
        resultHospital = db.session.query(Hospital).filter_by(caseName=oldName).all()
        for i in resultHospital:
            i.caseName = caseName

        caseU.caseName = caseName
        caseU.animalName = animalName
        caseU.diseaseName = diseaseName
        caseU.caseInfo = caseInfo
        caseU.videoUrl = videoUrl
        caseU.imageUrl = imageUrl
        caseU.processUrl1 = processUrl1
        caseU.processUrl2 = processUrl2
        caseU.processUrl3 = processUrl3
        caseU.info1 = info1
        caseU.info2 = info2
        caseU.info3 = info3
        db.session.commit()
        # json化data
        temp = {}
        temp["caseId"] = caseId
        temp["caseName"] = caseName
        temp["caseInfo"] = caseInfo
        temp["diseaseName"] = diseaseName
        temp["animalName"] = animalName
        temp["videoUrl"] = videoUrl
        temp["imageUrl"] = imageUrl
        temp["processUrl1"] = processUrl1
        temp["processUrl2"] = processUrl2
        temp["processUrl3"] = processUrl3
        temp["info1"] = info1
        temp["info2"] = info2
        temp["info3"] = info3

        data = []
        data.append(temp)
        return ops_renderJSON(msg="修改成功", data=data)

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

        allUsedMedicine = {}
        for i in result:
            caseName = i.caseName
            medicineStr = ''
            medicineList = []
            resultCaseMedicine = db.session.query(Casemedicine).filter_by(caseId=i.caseId).all()
            for j in resultCaseMedicine:
                curMedicineId = j.medicineId
                medicineD = db.session.query(Medicine).filter_by(medicineId=curMedicineId).first()
                medicineName = medicineD.name
                medicineList.append(medicineName)
                medicineStr = medicineStr + ' ' + medicineName
            # hospitalD = db.session.query(Hospital).filter_by(caseName=caseName).first()
            # if hospitalD != None:
            #     medicineList.append("住院费用")
            # 生成该病例使用过的药品名称键list
            medicineKeys = []
            for i1 in medicineList:
                if i1 not in medicineKeys:
                    medicineKeys.append(i1)
            medicineCount = {}
            for j1 in medicineKeys:
                medicineCount[j1] = medicineStr.count(j1)
            # if hospitalD != None:
            #     medicineCount["住院费用"] = hospitalD.pay
            allUsedMedicine["%s" % caseName] = medicineCount

        temp = {}
        data = []
        if (result != None):
            for i in result:
                temp["caseId"] = i.caseId
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
                temp["info1"] = i.info1
                temp["info2"] = i.info2
                temp["info3"] = i.info3
                temp["usedMedicine"] = allUsedMedicine["%s" % i.caseName]
                data.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=data)
        else:
            return ops_renderErrJSON(msg="查询失败，目前没有病例")


@case.route("/fuzzy", methods=['POST'])
def fuzzySearchCase():
    if request.method == 'POST':
        res = request.values
        page = res['page']
        per_page = res['per_page']
        caseName = res['caseName']
        if (page == ''):
            page = 1
        else:
            page = int(page)
        if (per_page == ''):
            per_page = 10
        else:
            per_page = int(per_page)
        result = db.session.query(Case).filter(Case.caseName.like('%%%%%s%%%%' % caseName)).limit(
            per_page).offset((page - 1) * per_page)
        temp = {}
        data = []
        if (result != None):
            for i in result:
                temp["caseId"] = i.caseId
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
                temp["info1"] = i.info1
                temp["info2"] = i.info2
                temp["info3"] = i.info3
                data.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=data)
        else:
            return ops_renderErrJSON(msg="查询失败，目前没有病例")


# 根据caseId删除病例
@case.route("/delete", methods=['POST'])
def deletecase():
    from init import db
    if request.method == 'POST':
        res = request.values
        caseId = res['caseId']
        caseD = db.session.query(Case).filter_by(caseId=caseId).first()
        if caseD == None:
            return ops_renderErrJSON(msg="目前没有该病例，请再次确认")
        caseInfo = caseD.caseInfo
        caseName = caseD.caseName
        diseaseName = caseD.diseaseName
        animalName = caseD.animalName
        videoUrl = caseD.videoUrl
        imageUrl = caseD.imageUrl
        processUrl1 = caseD.processUrl1
        processUrl2 = caseD.processUrl2
        processUrl3 = caseD.processUrl3
        info1 = caseD.info1
        info2 = caseD.info2
        info3 = caseD.info3
        temp = {}
        temp["caseId"] = caseId
        temp["caseName"] = caseName
        temp["caseInfo"] = caseInfo
        temp["diseaseName"] = diseaseName
        temp["animalName"] = animalName
        temp["videoUrl"] = videoUrl
        temp["imageUrl"] = imageUrl
        temp["processUrl1"] = processUrl1
        temp["processUrl2"] = processUrl2
        temp["processUrl3"] = processUrl3
        temp["info1"] = info1
        temp["info2"] = info2
        temp["info3"] = info3
        data = []
        data.append(temp)

        db.session.delete(caseD)
        db.session.commit()

        return ops_renderJSON(msg="删除成功", data=data)


@case.route("/addCaseMedicine", methods=['POST'])
def addCaseMedicine():
    from init import db
    if request.method == 'POST':
        res = request.values
        caseId = res['caseId']
        medicineName = res['medicineName']
        medicineCount = res['medicineCount']
        medicineCount = int(medicineCount)
        medicineD = db.session.query(Medicine).filter_by(name=medicineName).first()
        if medicineD == None:
            return ops_renderErrJSON(msg="没有这种药品，请确认后再添加")
        curMedicineId = medicineD.medicineId
        for i in range(medicineCount):
            model_caseMedicine = Casemedicine()
            model_caseMedicine.medicineId = curMedicineId
            model_caseMedicine.caseId = caseId
            db.session.add(model_caseMedicine)
        db.session.commit()
        temp = {}
        temp["caseId"] = caseId
        temp["medicineName"] = medicineName
        temp["medicineCount"] = medicineCount
        data = []
        data.append(temp)
        return ops_renderJSON(msg="病例添加药品成功", data=data)


@case.route("/animal",methods=["POST"])
def animal():
    auth = authRes(request)
    # auth = None
    if auth is not None:
        return auth
    # else后面接权限正常情况下的代码
    elif request.method == 'POST':
        req = request.values
        diseaseName = req['diseaseName']
        result = Case.query.filter_by(diseaseName = diseaseName).all()
        temp = {}
        animals = []
        if result is not None:
            for i in result:
                temp["animalId"] = i.animalId
                temp["animalName"] = i.animalName
                temp["imageUrl"] = i.imageUrl
                temp["caseId"] = i.caseId
                animals.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=animals)
        else:
            return ops_renderErrJSON(msg="查询失败，没有数据")


@case.route("/info",methods=["POST"])
def info():
    auth = authRes(request)
    # auth = None
    if auth is not None:
        return auth
    # else后面接权限正常情况下的代码
    elif request.method == 'POST':
        req = request.values
        caseId = req['caseId']
        result = Case.query.filter_by(caseId = caseId).first()
        animal = Animal.query.filter_by(animalId = result.animalId).first()
        case = {}
        if result and animal is not None:
            case["caseId"] = result.caseId
            case["animalName"] = result.animalName
            case["age"] = animal.age
            case["temper"] = animal.temper
            case["breathe"] = animal.breathe
            case["heartRate"] = animal.heartRate
            case["imageUrl"] = result.imageUrl
            case["caseinfo"] = result.caseInfo
            case["info1"] = result.info1
            case["processUrl1"] = result.processUrl1
            case["movieUrl"] = result.videoUrl
            case["info2"] = result.info2
            case["processUrl2"] = result.processUrl2
            case["info3"] = result.info3
            case["processUrl3"] = result.processUrl3
            return ops_renderJSON(msg="查询成功", data=case)
        else:
            return ops_renderErrJSON(msg="查询失败，没有数据")


