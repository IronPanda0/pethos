import decimal

from flask import Flask, Blueprint, render_template
from flask_login import LoginManager
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask.json import JSONEncoder as _JSONEncoder


class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        variable_start_string='%%',  # Default is '{{', I'm changing this because Vue.js uses '{{' / '}}'
        variable_end_string='%%',
    ))


app = CustomFlask(__name__,
                  static_folder="./templates/static",
                  template_folder="./templates",
                  )
# 此文件仅用于初始化配置

# 各种变量的配置文件，默认加载base_setting
app.config.from_pyfile("config/base_setting.py")
CORS(app)

# 创建数据库通讯对象
db = SQLAlchemy(app)

# 这里的redis用来存放token
redis_client = FlaskRedis()
redis_client.init_app(app)

