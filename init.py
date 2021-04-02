from flask import Flask, Blueprint, jsonify
from flask_login import LoginManager
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__,
            static_folder="./templates/static",
            template_folder="./templates",
            )
# 此文件仅用于初始化配置
CORS(app)

# 各种变量的配置文件，默认加载base_setting
app.config.from_pyfile("config/base_setting.py")

# 创建数据库通讯对象
db = SQLAlchemy( app )
