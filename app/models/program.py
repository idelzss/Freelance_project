from .base import BASE
from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship



class Program(BASE):
    __tablename__ = "programs"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    video_url = Column(Text, nullable=True)
    profession_id = Column(Integer, ForeignKey('professions.id'), nullable=False)