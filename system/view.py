from flask import Blueprint, request, make_response, render_template, jsonify
from sqlalchemy import text
import json
from init import db
from model.user import User

# 蓝图对象，前端页面
welcome = Blueprint('welcome', __name__)

@welcome.route('/vue')
def vue():
    return render_template("index.html")

@welcome.route('/')
def login():

    context = {}
    # sql = text('select * from `user`')
    # result = db.engine.execute(sql)
    # context['result'] = result
    context['admin'] = User.query.all()
    return render_template("index.html", **context)

# 比如： http://127.0.0.1:5000/manager
@welcome.route('/manager')
def manager():
    return "index of manager"


@welcome.route('/intern')
def intern():
    return "index of intern"


# 请求部分
# GET和POST请求
# 如果不写，methods默认为GET
@welcome.route('/get', methods=['GET'])
def get():
    # 以下语句在使得getvar可以获取前端返回的键为"user"的数据
    # 1. 现在,getvar为默认值"NoUser"
    # 2. 前端通过url返回数据，如：http://(域名)/get?user=JACK&password=123456
    # 3. 此时getvar="JACK"
    # NB：但是键"password"的值后台是拿不到的
    # 默认情况下type=str
    getvar = request.args.get("user", type=str, default="NoUser")
    # getargs将可以获取全部参数列表
    getargs = request.args
    return "请求方法：%s, 前端返回的键值对列表：%s，抓到的值：%s"%(request.method, getargs, getvar)


@welcome.route('/post', methods=['POST'])
def post():
    # 以下语句在使得postvar可以获取前端返回的键为"user"的数据
    postvar = request.form["user"] if "user" in request.form else 'No user was found'
    # postvar = request.form.get("user", type=str, default="NoUser")
    # getform将可以获取全部参数列表
    postform = request.form
    # 但是无法通过url传参给后端, POST请求中的表格数据是藏在前端的Body里的
    return "请求方法：%s, 前端返回的键值对列表：%s，抓到的值：%s"%(request.method, postform, postvar)


# -------------------后端请求传参---------------------
@welcome.route('/values', methods=['GET','POST'])
def values():
    # request.values无论是GET还是POST的数据都能拿到
    getall = request.values
    # 如果GET请求和POST请求都传了同键名的参数，那么request.values会优先拿GET请求的参数
    return getall.to_dict()


# -------------------后端请求传文件----------------------
@welcome.route('/upload', methods=['POST'])
def uploadfile():
    # request.file可以拿到POST请求中前端上传的文件列表
    file = request.files
    # jpg会拿到键名为"petjpg"的图片信息
    jpg = request.files['petjpg'] if "petjpg" in request.files else 'No image was found'
    # 文件通过前端里的form-data传到后端
    return "列表：%s,宠物图片：%s"%(file, jpg)


# 响应部分
# --------------------前端请求文本-------------------------
@welcome.route('/text')
def sendtext():
    response = make_response("文本内容", 200)
    return response


# --------------------前端请求json表单---------------------
@welcome.route('/json')
def sendjson():
    data = {"username": "JACK"}
    # json.dumps将符合格式的Python数据编码为json
    # response = make_response(json.dumps(data))
    # response.headers["Content-Type"] = "application/json"
    # 上下两段代码等价
    response = make_response(jsonify(data))
    return response


# --------------------前端请求html页面---------------------
@welcome.route('/html')
def sendhtml():
    return render_template("index.html")


# --------------------前端请求带参html页面1---------------------
@welcome.route('/htmlparam')
def sendhtmlwithparam():
    name = "JACK"
    # 前面的name对应前端，后面的name对应后端
    # 前端通过双花括号引用的方式取得参数：<p>name = {{ name }}</p>
    return render_template("index.html", name = name)


# --------------------前端请求带参html页面2---------------------
@welcome.route('/htmlparam2')
def sendhtmlwithparam2():
    name = "JACK"
    context = {"name": name}
    # 传进去一个字典，引号中的name对应前端变量名
    return render_template("index.html", **context)

# --------------------jinja2模板if和for语句---------------------
@welcome.route('/ifandfor')
def ifandfor():
    name = "JACK"
    context = {"name": name}
    # 上面这句等价于context["name"]=name
    context['name_list']={"MIKE",  "PETER"}
    context['MARRY'] = {"name":"MARRY", "password":"123456"}
    # 传进去一个字典，引号中的name对应前端变量名
    return render_template("index.html", **context)

