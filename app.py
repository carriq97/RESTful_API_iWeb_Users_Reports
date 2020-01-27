import flask_login
from flask import Flask, g
from social_flask_sqlalchemy.models import init_social

from resources.error_handler import errorBP
from resources.local.report_crud import reportBP
from resources.local.user_crud import userBP
from resources.models.db import db, db_session
from resources.models.user import User
from resources.online.location_openData import locationBP
from resources.online.parking_openData import parkingBP
from social_flask.routes import social_auth

from dbconfig import mysql

application = Flask(__name__)
application.config.from_object('aparcamalaga.settings')

db.init_app(application)
# mysql.init_app(application)

# Blueprints
application.register_blueprint(errorBP)

application.register_blueprint(reportBP)
application.register_blueprint(userBP)

application.register_blueprint(parkingBP)
application.register_blueprint(locationBP)

#OAuth
login_manager = flask_login.LoginManager()

login_manager.init_app(application)
application.register_blueprint(social_auth)
init_social(application, db_session)


@login_manager.user_loader
def load_user(userid):
    try:
        return User.query.get(int(userid))
    except (TypeError, ValueError):
        pass


@application.before_request
def global_user():
    g.user = flask_login.current_user


def inject_name(backend, user, response, *args, **kwargs):
    if 'given_name' in response:
        user.name = f"{response['given_name']} {response.get('family_name', '')}"[:45]
    else:
        user.name = user.username
