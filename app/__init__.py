import os
from flask import Flask, render_template
from dotenv import load_dotenv
from .models import create_db, session, User
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from .admin.routes import admin
from .employer.routes import employer


load_dotenv()

app = Flask(__name__, template_folder="templates")
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(employer, url_prefix='/employer')
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = os.getenv("STM")

Bootstrap(app)

login_manager = LoginManager()
login_manager.init_app(app)




create_db()
from . import routes
from .admin import routes