from flask_sqlalchemy import SQLAlchemy
from init import *
from system.view import welcome
from system.testModule.question import question
from system.caseModule.case import case
from system.caseModule.animal import animal
from system.caseModule.category import category
from system.caseModule.disease import disease
from system.testModule.test import test
from system.testModule.paper import paper
from system.userRole import userRole
from system.roomModule.room import room
from system.costModule.medicine import medicine
from system.costModule.fee import fee
from system.manager.managerCon import manager
# from flask_debugtoolbar import DebugToolbarExtension
from system.instance.view import instance
# from flask_debugtoolbar import DebugToolbarExtension
from interceptor.errorHandler import *
from common.urlmanager import UrlManager

# toolbar = DebugToolbarExtension(app)

app.config['JSON_AS_ASCII'] = False
# 蓝图注册
app.register_blueprint(welcome)
app.register_blueprint(instance)
app.register_blueprint(manager)
app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl, 'buildUrl')

app.register_blueprint(question)
app.register_blueprint(case)
app.register_blueprint(animal)
app.register_blueprint(category)
app.register_blueprint(disease)
app.register_blueprint(test)
app.register_blueprint(paper)
app.register_blueprint(userRole)
app.register_blueprint(room)
app.register_blueprint(medicine)
app.register_blueprint(fee)
app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl, 'buildUrl')
