from flask import Blueprint, request, make_response, render_template, jsonify
from flask_cors import CORS
from sqlalchemy import text
import json
from init import db
from model.paper import Paper
from model.question import Question
from model.paperquestion import Paperquestion
from common.Response import ops_renderErrJSON, ops_renderJSON

paper = Blueprint('paper', __name__, url_prefix='/paper')


@paper.route("/add", methods=['POST'])
def addPaper():
    if request.method == 'POST':
        req = request.values
        questionIDList = request.form.getlist('IdList')
        testName = req['testName']

        temp = {}
        data = []
        for i in questionIDList:
            result = Question.query.filter_by(questionId=i).first()
