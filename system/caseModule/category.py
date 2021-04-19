from flask import Blueprint, request, make_response, render_template, jsonify
from flask_cors import CORS
from sqlalchemy import text
import json
from init import db
from model.category import Category
from common.Response import ops_renderErrJSON, ops_renderJSON

category = Blueprint('categoryModule', __name__, url_prefix='/category')

@category.route("/add", methods=['GET', 'POST'])
def addCategory():
    # html文件修改为新建题目的文件
    if request.method == "GET":
        return render_template("提交分类.html")
    elif request.method == "POST":
        req = request.values
        # 暂时略过合法性检测
        categoryName = req['categoryName']
        categoryNameD = Category.query.filter_by(categoryName=categoryName).first()
        if categoryNameD:
            return ops_renderErrJSON(msg="相同分类已存在，请再换一个试试")
        # 注册写入数据库
        model_category = Category()
        model_category.categoryName = categoryName
        db.session.add(model_category)
        db.session.commit()
        # json化data
        temp = {}
        temp["categoryName"] = categoryName
        data = []
        data.append(temp)
        return ops_renderJSON(msg="添加成功", data=data)
    return "添加成功"


@category.route("/list", methods=['POST'])
def searchCategory():
    if request.method == 'POST':
        result = Category.query.all()
        temp = {}
        data = []
        if (len(result) != 0):
            for i in result:
                temp["categoryID"] = i.categoryID
                temp["categoryName"] = i.categoryName
                data.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=data)
        else:
            return ops_renderErrJSON(msg="查询失败，目前没有分类")

@category.route("/update", methods=['POST'])
def updateCategory():
    if request.method == 'POST':
        req = request.values
        categoryNameOld = req['categoryNameOld']
        categoryNameNew = req['categoryNameNew']
        categoryNameD = db.session.query(Category).filter_by(categoryName = categoryNameNew).first()
        if categoryNameD:
            return ops_renderErrJSON(msg="分类已经存在，请换一个再试试。")
        else:
            categoryNameU = db.session.query(Category).filter_by(categoryName = categoryNameOld).first()
            if categoryNameU != None:
                categoryNameU.categoryName = categoryNameNew
                db.session.commit()
                # json化data
                temp = {}
                temp["categoryName"] = categoryNameNew
                data = []
                data.append(temp)
                return ops_renderJSON(msg="修改成功", data=data)
            else:
                return ops_renderErrJSON(msg="不存在这个分类，无法修改")
    return "修改成功"
