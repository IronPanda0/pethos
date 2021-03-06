from flask_sqlalchemy import SQLAlchemy
from init import *
from system.view import welcome
from system.testModule.question import question
from system.caseModule.case import case
from system.caseModule.animal import animal
from system.caseModule.category import category
from system.caseModule.disease import disease
from system.costModule.executes import executes
from system.costModule.consumables import consumables
from system.testModule.test import test
from flask_debugtoolbar import DebugToolbarExtension
from interceptor.errorHandler import *
from common.urlmanager import UrlManager
toolbar = DebugToolbarExtension(app)

# 蓝图注册
app.register_blueprint(welcome)
app.register_blueprint(question)
app.register_blueprint(case)
app.register_blueprint(animal)
app.register_blueprint(category)
app.register_blueprint(disease)
app.register_blueprint(executes)
app.register_blueprint(consumables)
app.register_blueprint(test)
app.add_template_global( UrlManager.buildStaticUrl,'buildStaticUrl' )
app.add_template_global( UrlManager.buildUrl,'buildUrl' )