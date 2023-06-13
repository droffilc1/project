from time import timezone
from datetime import datetime
from sqlalchemy import true
from sqlalchemy.sql import func
from db import db
from flask_login import UserMixin

class UserModel(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.column(db.Integer, primary_key=True)
    username = db.column(db.String(80))
    firstname = db.column(db.Text(80), nullable=False, unique=False)    
    lastname = db.column(db.Text(80), nullable=False, unique=False)
    email = db.column(db.String(80), nullable=False, unique=False)
    password_hash = db.column(db.Text, nullable=False)