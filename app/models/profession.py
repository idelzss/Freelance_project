from .base import BASE
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import relationship


class Profession(BASE):
    __tablename__ = "professions"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    programs = relationship('Program', backref='profession')
    jobs = relationship('Job', backref='profession')