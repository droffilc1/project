from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import current_user, login_required, current_user
# from blogsite.models import ArticleModel, UserModel, CommentModel
from db import db

article = Blueprint("article", __name__)