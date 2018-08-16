from flask import Blueprint
from S10day132 import db
from S10day132.model import Users

us = Blueprint("us", __name__)


@us.route("/")
def index():
    # ret = db.session.query(Users).all()
    # ret = db.session.query(Users).first()
    # print(ret.name)
    return "O98K"