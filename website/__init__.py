from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = 'ATJMAI'

    # NOTE: if password is present : 'mysql://user:password@host/database'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/almai_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = False
    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    from .models import Alumni
    return app