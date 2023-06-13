import os
from flask import Flask
from db import db
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from models import ArticleModel, UserModel
from resources.user import auth as UserBlueprint
from resources.article import article as ArticleBlueprint
from resources.views import view as ViewBlueprint



# Generate current directory
base_dir = os.path.dirname(os.path.realpath(__file__))

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + \
            os.path.join(base_dir, 'blog.db')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = 'iLhqyLO3HtSpsE8cuQaj'	
    db.init_app(app)

    app.register_blueprint(ViewBlueprint)
    app.register_blueprint(ArticleBlueprint)
    app.register_blueprint(UserBlueprint)    

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
