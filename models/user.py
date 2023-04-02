#!/usr/bin/python3
"""This is the user class"""
from models.main_models import MainModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(MainModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    phone_number = Column(String(128), nullable=False)
    
    reviews = relationship('Review', cascade='all, delete', backref='user')
    # services = relationship('Service', cascade='all, delete', backref='user')
    payments = relationship('Payment', cascade='all, delete', backref='user')

   