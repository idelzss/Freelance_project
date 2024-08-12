from .base import BASE, session
from sqlalchemy import Column, String, Integer, Boolean
from flask_login import UserMixin


class User(BASE, UserMixin):
    __tablename__ = "users"


    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    phone = Column(String(30), nullable=False, unique=True)
    email_confirmed = Column(Boolean, nullable=True, default=True)
    admin = Column(Boolean, default=False, nullable=False)
    image_file = Column(String(20), nullable=False, default='default.jpg')
    password = Column(String(250), nullable=False, unique=True)
    user_type = Column(String(10), nullable=False, default='freelancer')