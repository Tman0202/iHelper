#!/usr/bin/python3
"""Defines the MainModel class."""
from uuid import uuid4
from datetime import datetime
import models

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


Base = declarative_base()


class MainModel:
    """
        Represents the MainModel class for all
        objects in the iHelper Clone Project
    """
    id = Column(
        String(60),
        primary_key=True,
        unique=True,
        nullable=False)

    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow())

    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow())


    def __init__(self, *args, **kwargs):
        """Base model initialization"""
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now()
        
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                if key == 'created_at' or key == 'updated_at':
                    time_format = '%Y-%m-%dT%H:%M:%S.%f'
                    setattr(self, key, datetime.strptime(value, time_format))
            

    def save(self):
        """Updates updated_at with the current datetime object"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        dico = self.__dict__.copy()
        dico["__class__"] = str(type(self).__name__)
        dico["created_at"] = self.created_at.isoformat()
        dico["updated_at"] = self.updated_at.isoformat()
        dico.pop("_sa_instance_state", None)
        return dico    
    
    def __str__(self):
        """Returns official string representation"""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)
  
    def delete(self):
        """Delete the current instance from storage."""
        models.storage.delete(self)