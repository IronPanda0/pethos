from www import app
from init import db
# 此文件仅用于运行项目
# pip install -r requirements.txt 安装依赖
# pip freeze >requirements.txt 更新依赖清单



if __name__ == '__main__':
    from model.user import User
    # 下列语句根据model在数据库里创建表
    # db.create_all()
# <<<<<<< HEAD
    app.run(host = "127.0.0.1",port=8000,debug=True)
# =======
#     app.run(host="127.0.0.1", port=8000, debug=True)
# >>>>>>> a88316635bfad30e4124c743db3f58697bab070a
