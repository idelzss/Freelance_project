from .base import BASE
import enum
from sqlalchemy import Column, String, Integer, Boolean, Enum
from flask_login import UserMixin

class UserTypeEnum(enum.Enum):
    freelancer = "freelancer"
    employer = "employer"


class User(BASE, UserMixin):
    __tablename__ = "users"


    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    phone = Column(String(30), nullable=False, unique=True)
    admin = Column(Boolean, default=False, nullable=False)
    password = Column(String(250), nullable=False, unique=True)
    user_type = Column(Enum(UserTypeEnum), nullable=False, default=UserTypeEnum.freelancer)