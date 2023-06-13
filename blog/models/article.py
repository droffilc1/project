from time import timezone
from datetime import datetime
from sqlalchemy import true
from sqlalchemy.sql import func
from db import db
from flask_login import UserMixin

class ArticleModel(db.Model):
    __tablename__ = "article"
    id = db.column(db.Integer, primary_key=True)
    title = db.column(db.String(550))
    bodytext = db.column(db.Text(3000), nullable=False, unique=False)
    author = db.column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    date_created = db.column(db.datetime(timezone=True), default=datetime.utcnow())
