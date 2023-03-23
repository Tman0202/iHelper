#!/usr/bin/python3
"""This is the review class"""
import models
from models.main_models import MainModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(MainModel, Base):
    """This is the class for Review
    Attributes:
        place_id: place id
        user_id: user id
        text: review description
    """
    __tablename__ = "reviews"

    service_id = Column(String(60), ForeignKey('service.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
    