from flask import Blueprint, request, make_response, render_template, jsonify, redirect, url_for
from flask_cors import CORS
from sqlalchemy import text
import json
from init import db, app
from model.task import Task
from model.taskProcess import Taskprocess
from common.Response import ops_renderErrJSON, ops_renderJSON

# created by lzy

# 蓝图对象，前端页面
role = Blueprint('role', __name__,url_prefix='/role')

@role.route('/show',methods = ['GET','POST'])
def task():
    if request.method == 'GET':
        req = request.args.get('role')

        #数据库查询
        task = Task.query.filter_by(role = req).all()
        temp1 = {}
        temp2 = {}
        temp3 = []
        data = []

        if (task != None):
            for i in task:
                #temp1存放一次任务的三个操作
                temp1['taskId'] = i.taskId
                temp1['taskName'] = i.taskName
                print(i.taskId)
                print(i.taskName)
                taskprocess = Taskprocess.query.filter_by(taskId = i.taskId).all()
                #temp2存放具体操作（前，中，后）
                t = 1
                for j in taskprocess:
                    temp2['taskProcessId'] = j.taskProcessId
                    temp2['content'] = j.content
                    temp2['imgUrl'] = j.imgUrl
                    temp2['process'] = j.process
                    t = t + 1
                    temp3.append(temp2.copy())
                temp1['item'] = temp3.copy()
                temp3 = []

                data.append(temp1.copy())
            return ops_renderJSON(msg="学习信息成功返回", data=data)
        else:
            return ops_renderErrJSON(msg="未查询到学习信息")




