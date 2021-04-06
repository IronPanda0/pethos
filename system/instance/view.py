from flask import Blueprint, request, make_response, render_template, jsonify, redirect, url_for
from flask_cors import CORS
from init import db, app
from model.user import User
from common.Response import ops_renderErrJSON, ops_renderJSON

CORS(app, supports_credentials=True)
# 蓝图对象，前端页面
instance = Blueprint('instance', __name__, url_prefix="/Case")


@instance.route("/info", methods = ['GET','POST'])
def getinfo():
    req = request.values
    return