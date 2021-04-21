from flask import Blueprint, request, make_response, render_template, jsonify, redirect, url_for
from flask_cors import CORS
from sqlalchemy import text
import json
from init import db, app
from model.room import Room
from model.item import Item
from common.Response import ops_renderErrJSON, ops_renderJSON

# created by lzy

# 蓝图对象，前端页面
map = Blueprint('map', __name__,url_prefix='/map')

#点击医院导览后
#返回所有科室信息及物品信息
@map.route('/show',methods = ['GET','POST'])
def hos_map():
    if request.method == 'GET':
        #数据库查询
        room = Room.query.all()

        temp1 = {}
        temp2 = {}
        data = []
        if not room:
            return ops_renderErrJSON(msg="不存在科室，请重试")
        else:
            for i in room:
                temp1['title'] = i.roomName
                temp1['id'] = i.roomId
                temp1['imgUrl'] = i.imgUrl
                temp1['employee'] = i.employee
                temp1['intro'] = i.intro
                r = i.roomId
                item = Item.query.filter_by(roomId = r).all()
                temp1['items'] = []
                if (item != None):
                    for j in item:
                        temp2['itemName'] = j.itemName
                        temp2['intro'] = j.intro
                        temp2['imgUrl'] = j.videoUrl
                        temp1['items'].append(temp2.copy())
                data.append(temp1.copy())
            return ops_renderJSON(msg="科室信息返回成功",data = data)



    


