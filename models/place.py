#!/usr/bin/python3
"""This is the city class"""
import models
from models.main_models import MainModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Place(MainModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    # initialize class for file/db storage type
    __tablename__ = 'place'
    name = Column(String(128), nullable=False)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    service = relationship('Service', cascade='all, delete', backref='place')   
