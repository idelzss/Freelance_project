from .base import BASE
import enum
from sqlalchemy import Column, String, Integer, ForeignKey, Text, DateTime, Enum
from datetime import datetime
from sqlalchemy.orm import relationship


class StatusEnumJob(enum.Enum):
    not_done = "Not done"
    submitted = "Submitted"



class Job(BASE):
    __tablename__ = "jobs"


    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    profession_id = Column(Integer, ForeignKey("professions.id"), nullable=False)
    employer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    freelancer_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    status = Column(Enum(StatusEnumJob), default=StatusEnumJob.not_done, nullable=False)

    employer = relationship("User", foreign_keys=[employer_id])
    profession = relationship("Profession", foreign_keys=[profession_id])
