from init import db
# 用这个语句将数据库的表结构抓到py文件里
# flask-sqlacodegen "mysql://root:5c7986b3E@127.0.0.1/mysql" --tables user --outfile "model/XX.py" --flask


# User(大小写不区分）对应数据库里的表名，Id、Username、Password对应列名
class User( db.Model ):
    __tablename__="user"

    Id = db.Column (db.String(10), primary_key=True)
    Username = db.Column( db.String( 12 ) )


# UserP继承的是User类，那么UserP也会去查询数据库中的"user"表
# 所以UserP会查出Id、Username和Password
class UserP (User):
    Password = db.Column(db.String(18))