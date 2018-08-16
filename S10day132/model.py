from sqlalchemy import Column, Integer, String
from S10day132 import db

# db.Model 调用的SQLAlchemy里的declarative_base()
class Users(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=False)
    gender = Column(String(32))

class Girl(db.Model):
    __tablename__ = 'girl'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=False)
    gender = Column(String(32))


