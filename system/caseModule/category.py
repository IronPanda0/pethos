from flask import Blueprint, request, make_response, render_template, jsonify
from flask_cors import CORS
from sqlalchemy import text
import json
from init import db
from model.category import Category
from common.Response import ops_renderErrJSON, ops_renderJSON

category = Blueprint('categoryModule', __name__,url_prefix='/categoryModule')


@category.route("/add", methods=['GET', 'POST'])
def addcategory():
    # html文件修改为新建题目的文件
    if request.method == "GET":
        return render_template("提交分类.html")
    elif request.method == "POST":
        req = request.values
        # 暂时略过合法性检测
        categoryName= req['categoryName']
        categoryNameD = Category.query.filter_by(categoryName = categoryName).first()
        if categoryNameD:
            return ops_renderErrJSON(msg="相同分类已存在，请再换一个试试")
        # 注册写入数据库
        model_category = Category()
        model_category.categoryName = categoryName
        db.session.add(model_category)
        db.session.commit()
        return ops_renderErrJSON(msg = "添加成功")
    return "添加成功"