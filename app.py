from flask import Flask
from dbconfig import mysql
from api.report_crud import reportBP
from api.user_crud import userBP
from api.error_handler import errorBP
from api.openData import openDataBP


application = Flask(__name__)

# MySQL configurations
application.config['MYSQL_USER'] = 'root'
application.config['MYSQL_PASSWORD'] = 'password'
application.config['MYSQL_DB'] = 'iweb'
application.config['MYSQL_HOST'] = '127.0.0.1'
mysql.init_app(application)

# Blueprints
application.register_blueprint(reportBP)
application.register_blueprint(userBP)
application.register_blueprint(errorBP)
application.register_blueprint(openDataBP)
