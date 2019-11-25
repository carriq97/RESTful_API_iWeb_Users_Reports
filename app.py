from flask import Flask

from app.api.report_crud import reportBP
from app.api.user_crud import userBP
from app.api.error_handler import errorBP

application = Flask(__name__)
application.register_blueprint(reportBP)
application.register_blueprint(userBP)
application.register_blueprint(errorBP)
