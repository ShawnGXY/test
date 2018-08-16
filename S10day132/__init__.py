from flask import Flask
from flask_session import Session

# 第一步导入SQLAlchemy
# 必须在蓝图之前
from flask_sqlalchemy import SQLAlchemy
# 第二步实例化
db = SQLAlchemy()



from .views.user import us

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings.MyConfig")
    app.register_blueprint(us)
    # Session
    # Session(app)

    db.init_app(app)

    return app