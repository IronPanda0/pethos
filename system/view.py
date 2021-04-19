from flask import Blueprint, request, make_response, render_template, jsonify, redirect, url_for
from flask_cors import CORS
from common.DataHelper import tokenGen, storeInRedis, getFromRedis, removeFromRedis
from init import db, app
from model.user import User
from common.Response import ops_renderErrJSON, ops_renderJSON, ops_renderIllegalJSON
from common.userAuth import *

CORS(app, supports_credentials=True)
# 蓝图对象，前端页面
welcome = Blueprint('welcome', __name__)


@welcome.route('/', methods=['GET', 'POST'])
def index():
    if request.values.has_key('entrance'):
        if request.method == "GET":
            if request.values['entrance'] == "user":
                return render_template("index_f.html")
            elif request.values['entrance'] == "manager":
                return render_template("index_b.html")
    return render_template('index.html')


@welcome.route('/login', methods=['POST'])
def loginConfirm():
    # 以下进行登录逻辑
    req = request.values
    username = req['username']
    password = req['password']
    print(username)
    # 判断用户名和密码合法性
    if username is None or len(username) < 1:
        return ops_renderErrJSON(msg="请输入正确的登录用户名~~")
    if password is None or len(password) < 6:
        return ops_renderErrJSON(msg="请输入正确的登录密码，并且不能小于6个字符~~")
    # 以下为查询语句，first()表示返回查到符合条件的第一条数据
    userD = User.query.filter_by(userName=username).first()
    if not userD:
        return ops_renderErrJSON(msg="用户名或密码错误-1")
    if userD.passWord != password:
        return ops_renderErrJSON(msg="用户名或密码错误-2")
    if userD.authority != 2:
        return ops_renderErrJSON(msg="用户名或密码错误-1")
    # user用来生成token
    user = {
        "userId": userD.userId,
        "username": userD.userName,
        "auth": userD.authority
    }
    token = tokenGen(user)
    # 调用redis服务器保存token
    storeInRedis(userD.userId, token, expire=3600 * 24 * 7)
    # 返回给前端的token值，需要前端保存，每次请求数据都要检查
    res = make_response(ops_renderJSON(msg="登录成功~~", data={"token": token}))

    # 这里删除操作成功
    # removeFromRedis(userD.userId)

    # 这里拿到redis里根据用户Id存的token，并且一周后自动清除token
    # 尝试获取redis里的值
    print(getFromRedis(userD.userId))
    return res


@welcome.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        req = request.values
        username = req['username']
        password = req['password']
        checkpwd = req['checkpwd']
        if username is None or len(username) < 1:
            return ops_renderErrJSON(msg="请输入正确的登录用户名~~")
        if password is None or len(password) < 6:
            return ops_renderErrJSON(msg="请输入正确的登录密码，并且不能小于6个字符~~")
        if password != checkpwd:
            return ops_renderErrJSON(msg="两次密码不一致，请检查无误再操作~~")
        #         以下为查询语句，first()表示返回查到符合条件的第一条数据
        #         找到第一个同名的用户名
        userD = User.query.filter_by(userName=username).first()
        if userD:
            return ops_renderErrJSON(msg="用户名已经存在，请换一个再试试。")
        # 创建一个用户实例
        model_user = User()
        model_user.userName = username
        model_user.passWord = password
        model_user.mail = req['email']
        # 默认权限为2，即实习生
        model_user.authority = 2

        # 将实例写入数据库
        db.session.add(model_user)
        db.session.commit()
        return ops_renderJSON(msg="注册成功~~")
    return ops_renderErrJSON()


@welcome.route("/mlogin", methods=["POST"])
def mLogin():
    req = request.values
    username = req['username']
    password = req['password']
    print(username)
    # 判断用户名和密码合法性
    if username is None or len(username) < 1:
        return ops_renderErrJSON(msg="请输入正确的登录用户名~~")
    if password is None or len(password) < 6:
        return ops_renderErrJSON(msg="请输入正确的登录密码，并且不能小于6个字符~~")
    # 以下为查询语句，first()表示返回查到符合条件的第一条数据
    userD = User.query.filter_by(userName=username).first()
    if not userD:
        return ops_renderErrJSON(msg="用户名或密码错误-1")
    if userD.passWord != password:
        return ops_renderErrJSON(msg="用户名或密码错误-2")
    if userD.authority != 1:
        return ops_renderIllegalJSON()
    # user用来生成token
    user = {
        "userId": userD.userId,
        "username": userD.userName,
        "auth": userD.authority
    }
    token = tokenGen(user)
    # 调用redis服务器保存token
    storeInRedis(userD.userId, token, expire=3600 * 24 * 7)
    # 返回给前端的token值，需要前端保存，每次请求数据都要传给后端
    res = make_response(ops_renderJSON(msg="登录成功~~", data={"token": token}))
    return res


@welcome.route("/mregister", methods=["POST"])
def mRegister():
    if request.method == "POST":
        req = request.values
        username = req['username']
        password = req['password']
        checkpwd = req['checkpwd']
        if username is None or len(username) < 1:
            return ops_renderErrJSON(msg="请输入正确的登录用户名~~")
        if password is None or len(password) < 6:
            return ops_renderErrJSON(msg="请输入正确的登录密码，并且不能小于6个字符~~")
        if password != checkpwd:
            return ops_renderErrJSON(msg="两次密码不一致，请检查无误再操作~~")
        #         以下为查询语句，first()表示返回查到符合条件的第一条数据
        #         找到第一个同名的用户名
        userD = User.query.filter_by(userName=username).first()
        if userD:
            return ops_renderErrJSON(msg="用户名已经存在，请换一个再试试。")
        # 创建一个用户实例
        model_user = User()
        model_user.userName = username
        model_user.passWord = password
        # 默认权限为1，即管理员
        model_user.authority = 1
        # 将实例写入数据库
        db.session.add(model_user)
        db.session.commit()
        return ops_renderJSON(msg="管理员添加成功！")
    return ops_renderErrJSON()


# 登出前端写，这里做token的处理
@welcome.route("/logout", methods =["POST"])
def logout():
    userId = request.values["userId"] if "userId" in request.values else None
    token = request.values["token"] if "token" in request.values else None
    data = {
        "userId": userId,
        "token": token
    } if userId and token is not None else None
    auth = authCheck(data)
    if not auth:
        app.logger.info("权限不足，用户id:%s的登录态无效"%userId)
        return redirect(url_for("welcome.index"))
    # else后面接权限正常情况下的代码
    else:
        removeFromRedis(userId)
        return ops_renderJSON(msg="用户已登出!")




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
    return "请求方法：%s, 前端返回的键值对列表：%s，抓到的值：%s" % (request.method, getargs, getvar)


@welcome.route('/post', methods=['POST'])
def post():
    # 以下语句在使得postvar可以获取前端返回的键为"user"的数据
    postvar = request.form["user"] if "user" in request.form else 'No user was found'
    # postvar = request.form.get("user", type=str, default="NoUser")
    # getform将可以获取全部参数列表
    postform = request.form
    # 但是无法通过url传参给后端, POST请求中的表格数据是藏在前端的Body里的
    return "请求方法：%s, 前端返回的键值对列表：%s，抓到的值：%s" % (request.method, postform, postvar)


# -------------------后端请求传参---------------------
@welcome.route('/values', methods=['GET', 'POST'])
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
    return "列表：%s,宠物图片：%s" % (file, jpg)


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
    return render_template("index.html", name=name)


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
    context['name_list'] = {"MIKE", "PETER"}
    context['MARRY'] = {"name": "MARRY", "password": "123456"}
    # 传进去一个字典，引号中的name对应前端变量名
    return render_template("index.html", **context)
