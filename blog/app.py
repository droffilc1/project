import os
from flask import Flask
from db import db

# Generate current directory
base_dir = os.path.dirname(os.path.realpath(__file__))

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + \
            os.path.join(base_dir, 'blog.db')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = 'iLhqyLO3HtSpsE8cuQaj'	
    db.init_app(app)
    

    return app
