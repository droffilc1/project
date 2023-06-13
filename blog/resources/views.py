from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from models import ArticleModel
from flask_login import current_user, login_required
from db import db


view = Blueprint("view", __name__)

# Home route
@view.route('/')
@view.route('index')
def index():
    articles = ArticleModel.query.all()
    return render_template("index.html", user=current_user, articles=articles)

# About route
@view.route('/about')
def about():
    return render_template('about.html')

# Contact route
@view.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash('We appreciate the feedback, be on the lookout for our response', category='success')
    
    return render_template("contact.html", current_user=current_user)

# Publish route
@view.route('/publish', methods=["GET", "POST"])
def publish():
    if request.method == "POST":
        title = request.form.get("title")
        bodytext = request.form.get("bodytext")

        if not title and not bodytext:
            flash("Please fill in the title and bodytext to proceed.")
        else:
            article = ArticleModel(title=title, bodytext=bodytext, author=current_user.id)
            db.session.add(article)
            db.session.commit()
            flash("Your articke has been succesfully published.", category='success')
            return redirect(url_for("view.index"))
    
    return render_template("punlish.html")

