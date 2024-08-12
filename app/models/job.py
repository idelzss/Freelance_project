from .base import BASE
from sqlalchemy import Column, String, Integer, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime




class Job(BASE):
    __tablename__ = "jobs"


    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    job_type = Column(String(50), nullable=False)
    profession_id = Column(Integer, ForeignKey('professions.id'), nullable=False)
    employer_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    freelancer_id = Column(Integer, ForeignKey('users.id'))
    date_posted = Column(DateTime, nullable=False, default=datetime.utcnow)
    employer = relationship('User', foreign_keys=[employer_id], backref='posted_jobs')
    freelancer = relationship('User', foreign_keys=[freelancer_id], backref='assigned_jobs')

