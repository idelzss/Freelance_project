from .base import BASE
from sqlalchemy import Column, String, Integer, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class Application(BASE):
    __tablename__ = "applications"


    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey('jobs.id'), nullable=False)
    freelancer_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date_applied = Column(DateTime, nullable=False, default=datetime.utcnow)
    status = Column(String(50), nullable=False, default='Pending')  # 'Pending', 'Accepted', 'Rejected'
    job = relationship('Job', backref=('applications'))
    freelancer = relationship('User', backref=('applications'))