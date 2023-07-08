from sqlalchemy import Column, String, Text, DateTime, Integer, Boolean
from datetime import datetime
from app.core.db import Base


class ProjectDonation(Base):
    __abstract__ = True

    full_amount = Column(Integer)
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.now)
    close_date = Column(DateTime)


class CharityProject(ProjectDonation):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)