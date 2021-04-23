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
    if request.method == "POST":
        req = request.values
        roomName = req['roomName']
        employee = req['employee']
        intro = req['intro']
        imgUrl = req['imgUrl']
        # 略过数据合法性检测
        roomNameD = Room.query.filter_by(roomName=roomName).first()
        if (roomNameD):
            return ops_renderErrJSON(msg="相同科室名已存在，请再换一个试试")
        # 写入数据库
        model_room = Room()
        model_room.roomName = roomName
        model_room.employee = employee
        model_room.intro = intro
        model_room.imgUrl = imgUrl
        db.session.add(model_room)
        db.session.commit()
        temp = {}
        temp["roomName"] = roomName
        temp["intro"] = intro
        temp["employee"] = employee
        temp["imgUrl"] = imgUrl
        data = []
        data.append(temp)
        return ops_renderJSON(msg="添加成功", data=data)
    return "添加成功"


@room.route("/update", methods=['POST'])
def updateRoom():
    if request.method == 'POST':
        req = request.values
        roomId = req['roomId']
        roomNameNew = req['roomNameNew']
        employee = req['employee']
        intro = req['intro']
        imgUrl = req['imgUrl']
        roomNameD = db.session.query(Room).filter_by(roomName=roomNameNew).first()
        if roomNameD:
            return ops_renderErrJSON(msg="相同科室名已经存在，请换一个再试试。")
        else:
            roomU = db.session.query(Room).filter_by(roomId=roomId).first()
            if roomU != None:
                roomU.roomName = roomNameNew
                roomU.employee = employee
                roomU.intro = intro
                roomU.imgUrl = imgUrl
                db.session.commit()
                # json化data
                temp = {}
                temp["roomName"] = roomNameNew
                temp["employee"] = employee
                temp["intro"] = intro
                temp["imgUrl"] = imgUrl
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
        roomId = res['roomId']
        roomD = db.session.query(Room).filter_by(roomId=roomId).first()
        if roomD == None:
            return ops_renderErrJSON(msg="目前没有该科室，请再次确认")
        roomName = roomD.roomName
        intro = roomD.intro
        employee = roomD.employee
        imgUrl = roomD.imgUrl

        temp = {}
        temp["roomName"] = roomName
        temp["intro"] = intro
        temp["employee"] = employee
        temp["imgUrl"] = imgUrl
        data = []
        data.append(temp)

        db.session.delete(roomD)
        db.session.commit()

        return ops_renderJSON(msg="删除成功", data=data)


@room.route("/list", methods=['POST'])
def listRoom():
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
        result = Room.query.limit(per_page).offset((page - 1) * per_page)
        temp = {}
        data = []
        if (result.count() != 0):
            for i in result:
                temp["roomName"] = i.roomName
                temp["intro"] = i.intro
                temp["employee"] = i.employee
                temp["imgUrl"] = i.imgUrl
                data.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=data)
        else:
            return ops_renderErrJSON(msg="查询失败，目前没有药品")
