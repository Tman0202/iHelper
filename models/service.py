#!/usr/bin/python3
""" Service Module for iHelper project """
from models.main_models import MainModel, Base
from sqlalchemy import Column, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
import models

class Service(MainModel, Base):
    __tablename__ = 'service'
    
    name = Column(String(128), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    describtion = Column(String(128), nullable=False)
    review = relationship('Review', cascade='all, delete', backref='service')
    # user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    request = relationship('Request', cascade='all, delete', backref='service')
    place_id = Column(String(60), ForeignKey('place.id'), nullable=False)
    # make it service provider