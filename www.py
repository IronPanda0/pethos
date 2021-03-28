from flask_sqlalchemy import SQLAlchemy
from init import *
from system.view import welcome
from flask_debugtoolbar import DebugToolbarExtension
from interceptor.errorHandler import *

toolbar = DebugToolbarExtension(app)

# 蓝图注册

app.register_blueprint(welcome)
