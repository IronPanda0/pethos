from flask import Blueprint, request, make_response, render_template, jsonify
from flask_cors import CORS
from sqlalchemy import text
import json
from model.fee import Fee
from model.case import Case
from model.medicine import Medicine
from model.casemedicine import Casemedicine
from common.Response import ops_renderErrJSON, ops_renderJSON
from datetime import datetime, time

fee = Blueprint('fee', __name__, url_prefix='/fee')

@fee.route("/list", methods=['POST'])
def listFee():
    if request.method == "POST":
        from init import db
        resultCase = db.session.query(Case).all()
        tempMedicine = {}

        for i in resultCase:
            total = 0
            resultCaseMedicine = db.session.query(Casemedicine).filter_by(caseId=i.caseId).all()
            for j in resultCaseMedicine:
                curMedicineId = j.medicineId
                medicineD = db.session.query(Medicine).filter_by(medicineId=curMedicineId).first()
                total += medicineD.pay
            model_fee = Fee()
            model_fee.caseId = i.caseId
            model_fee.caseName = i.caseName
            model_fee.count = total
            db.session.add(model_fee)
        db.session.commit()
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
        result = Fee.query.limit(per_page).offset((page - 1) * per_page)
        temp = {}
        data = []
        if (result != None):
            for i in result:
                temp["caseId"] = i.caseId
                temp["caseName"] = i.caseName
                temp["count"] = i.count
                data.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=data)
        else:
            return ops_renderErrJSON(msg="查询失败，目前没有费用")
