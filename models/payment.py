#!/usr/bin/python3
""" Payment Module for iHelper project """
from models.main_models import MainModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Numeric

class Payment(MainModel, Base):
   __tablename__ = 'payments'
   payment_status = Column(String(20), nullable=False, default='pending')
   amount = Column(Numeric(10, 2), nullable=False)
   # service_id = Column(String(60), ForeignKey('services.id'), nullable=False)
   
   user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
   request_id = Column(String(60), ForeignKey('requests.id'), nullable=False)

   __table_args__ = {'extend_existing': True}