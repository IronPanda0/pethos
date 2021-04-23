from flask import Blueprint, request, make_response, render_template, jsonify
from flask_cors import CORS
from sqlalchemy import text
import json
from model.fee import Fee
from model.room import Room
from common.Response import ops_renderErrJSON, ops_renderJSON
from datetime import datetime, time

fee = Blueprint('fee', __name__, url_prefix='/fee')


@fee.route("/add", methods=['POST'])
def addmeMicine():
    from init import db
    if request.method == "POST":
        req = request.values
