from sqlalchemy import Column, Text, Integer, ForeignKey
from app.models.charity_project import ProjectDonation


class Donation(ProjectDonation):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)
