<<<<<<< HEAD

=======
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af
from flask import Flask, Blueprint, render_template
from flask_login import LoginManager
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,
            static_folder="./templates/dist/static",
            template_folder="./templates/dist",
            )
# cors = CORS(app, resources={"/api/*": {"origins": "*"}})

# 此文件仅用于初始化配置

# qaq
# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
#     return render_template("index.html")

# 各种变量的配置文件，默认加载base_setting
app.config.from_pyfile("config/base_setting.py")
CORS(app)

# 创建数据库通讯对象
db = SQLAlchemy( app )
