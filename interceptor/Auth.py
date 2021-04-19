from init import app
from flask import request, g
from model.user import User


@app.before_request
def before_request(itemId):
    if request.path=="/":
        return
    app.logger.info("--------before_request--------")
    g.current_user = None
    return
