from flask import Blueprint, request, make_response, render_template, jsonify
from flask_cors import CORS
from sqlalchemy import text
import json
from init import db
from model.room import Room
from common.Response import ops_renderErrJSON, ops_renderJSON
from datetime import datetime, time

room = Blueprint('room', __name__, url_prefix='/room')


@room.route("/add", methods=['POST'])
def addRoom():
    if request.method == "GET":
        return render_template("新增room.html")
    elif request.method == "POST":
        req = request.values
        roomName = req['roomName']
        employee = req['employee']
        intro = req['intro']
        # 略过数据合法性检测
        roomNameD = Room.query.filter_by(roomName=roomName).first()
        if (roomNameD):
            return ops_renderErrJSON(msg="相同科室已存在，请再换一个试试")
        # 写入数据库
        model_room = Room()
        model_room.roomName = roomName
        model_room.employee = employee
        model_room.intro = intro
        db.session.add(model_room)
        db.session.commit()
        temp = {}
        temp["roomName"] = roomName
        temp["intro"] = intro
        temp["employee"] = employee
        data = []
        data.append(temp)
        return ops_renderJSON(msg="添加成功", data=data)
    return "添加成功"


@room.route("/update", methods=['POST'])
def updateRoom():
    if request.method == 'POST':
        req = request.values
        roomNameOld = req['roomNameOld']
        roomNameNew = req['roomNameNew']
        employee = req['employee']
        intro = req['intro']
        roomNameD = db.session.query(Room).filter_by(roomName=roomNameNew).first()
        if roomNameD:
            return ops_renderErrJSON(msg="科室已经存在，请换一个再试试。")
        else:
            roomNameU = db.session.query(Room).filter_by(roomName=roomNameOld).first()
            if roomNameU != None:
                roomNameU.roomName = roomNameNew
                roomNameU.employee = employee
                roomNameU.intro = intro
                db.session.commit()
                # json化data
                temp = {}
                temp["roomName"] = roomNameNew
                temp["employee"] = employee
                temp["intro"] = intro
                data = []
                data.append(temp)
                return ops_renderJSON(msg="修改成功", data=data)
            else:
                return ops_renderErrJSON(msg="不存在这个科室，无法修改")
    return "修改成功"


# 根据roomName删除科室
@room.route("/delete", methods=['POST'])
def deleteRoom():
    from init import db
    if request.method == 'POST':
        res = request.values
        roomName = res['roomName']
        roomNameD = db.session.query(Room).filter(Room.roomName == roomName).first()
        if roomNameD == None:
            return ops_renderErrJSON(msg="目前没有该科室，请再次确认")
        intro = roomNameD.intro
        employee = roomNameD.employee

        temp = {}
        temp["roomName"] = roomName
        temp["intro"] = intro
        temp["employee"] = employee
        data = []
        data.append(temp)

        db.session.delete(roomNameD)
        db.session.commit()

        return ops_renderJSON(msg="删除成功", data=data)


@room.route("/list", methods=['POST'])
def listRoom():
    if request.method == 'POST':
        res = request.values
        page = int(res['page'])
        per_page = int(res['per_page'])
        if (page == None):
            page = 1
        if (per_page == None):
            per_page = 10
        result = Room.query.limit(per_page).offset((page - 1) * per_page)
        temp = {}
        data = []
        if (result != None):
            for i in result:
                temp["roomName"] = i.roomName
                temp["intro"] = i.intro
                temp["employee"] = i.employee
                data.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=data)
        else:
            return ops_renderErrJSON(msg="查询失败，目前没有药品")
