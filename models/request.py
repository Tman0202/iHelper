#!/usr/bin/python3
""" Request Module for iHelper project """
from models.main_models import MainModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Numeric

class Request(MainModel, Base):
   __tablename__ = 'requests'
   user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
   Request_status = Column(String(20), nullable=False, default='active')

   service_id = Column(String(60), ForeignKey('service.id'), nullable=False)
   # payment_id = Column(String(60), ForeignKey('payments.id'), nullable=False)
   
   payments = relationship('Payment', cascade='all, delete', backref='request')