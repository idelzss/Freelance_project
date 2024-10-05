from .base import BASE
import enum
from sqlalchemy import Column, String, Integer, ForeignKey, Text, DateTime, Enum

class StatusEnumSubmission(enum.Enum):
    not_done = "Not done"
    submitted = "Submitted"



class Submission(BASE):
    __tablename__ = "submissions"
    id = Column(Integer, primary_key=True)
    description = Column(Text, nullable=False)
    GitHub_Url = Column(Text, nullable=False)
    freelancer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(Enum(StatusEnumSubmission), default=StatusEnumSubmission.submitted, nullable=False)
    employer_id = Column(Integer, ForeignKey("users.id"), nullable=False)