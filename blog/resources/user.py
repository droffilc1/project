from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
# from flask_smorest import Blueprint, abort
from db import db
# from blogsite.models import UserModel
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash


user = Blueprint("user", __name__)