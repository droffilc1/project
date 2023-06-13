from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import current_user, login_required, current_user
from models import ArticleModel, UserModel, CommentModel
from db import db

article = Blueprint("article", __name__)

# Edit route
@article.route("/edit/<article_id>")
@login_required
def edit(article_id):
    article = ArticleModel.query.filter_by(id=article_id).first()
    if request.method == "POST":
        title = request.form.get("title")
        bodytext = request.form.get("bodytext")

        if not article:
            flash("We can't get your article. Try creating and publishing one.", category='error')
        elif current_user.id != article.author:
            flash("You are not allowed to make changes to this article.", category='error')
        else:
            article.title = title
            article.bodytext = bodytext
            db.session.commit()
            flash("Your article has been successfully edited.")
        return redirect(url_for("view.index"))

    return render_template("edit.html", article=article)

# Delete route
@article.route("/delete/<article_id>")
def delete(article_id):
    article = ArticleModel.query.filter_by(id=article_id).first()

    if not article:
        flash("This article does not exist.", category='error')
    elif current_user.id != article.author:
        flash("You are not allowed to delete this article.")
    else:
        db.session.delete(article)
        db.session.commit()
        flash("Article deleted successfully.", category='success')
        return redirect(url_for("view.index"))



        