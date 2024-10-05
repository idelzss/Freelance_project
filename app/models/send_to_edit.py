from .base import BASE
from sqlalchemy import Column, Integer, Text, ForeignKey


class Edit(BASE):
    __tablename__ = "edits"
    id = Column(Integer, primary_key=True)
    description = Column(Text, nullable=False)
    freelancer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    employer_id = Column(Integer, ForeignKey("users.id"), nullable=False)