from S10day132 import db, create_app
from S10day132.model import *
# 一定要导入models 否则找不到表创建不出来
app = create_app()
from flask import Flask
# Flask.app_context()
app_ctx = app.app_context()


# __enter__ with app_ctx 返回的 push
# 把App,g 通过LocalStack放入Local
# 离线脚步
with app_ctx:
    db.create_all()
    # db.drop_all()