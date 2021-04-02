# 公用配置文件
# 当debug为True，可以用app.logger.info("xxx")进行日志打印调试
DEBUG = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ENCODING = "utf8mb4"
SECRET_KEY = "123456"
<<<<<<< HEAD
# <<<<<<< HEAD
SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost/coursedb"
# =======
# SQLALCHEMY_DATABASE_URI = "mysql://root:123456@localhost/courseDB"
# >>>>>>> a88316635bfad30e4124c743db3f58697bab070a
=======
SQLALCHEMY_DATABASE_URI = "mysql://root:123456@localhost/courseDB"
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af

DOMAIN = {"www":"http://127.0.0.1:5000"}
