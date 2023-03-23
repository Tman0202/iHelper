#!/usr/bin/python3
"""This is the state class"""
from models.main_models import MainModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ


class City(MainModel, Base):
    """This is the class for State
    Attributes:
        __tablename__: name of MySQL table
        name: input name
    """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)

    if environ['IHELPER_TYPE_STORAGE'] == 'db':
        places = relationship('Place', cascade='all, delete', backref='city')
    else:
        @property
        def places(self):
            """Getter method for cities
            Return: list of cities with state_id equal to self.id
            """
            from models import storage
            from models.place import Place
            # return list of City objs in __objects
            places_dict = storage.all(Place)
            cities_list = []

            # copy values from dict to list
            for place in places_dict.values():
                if place.city_id == self.id:
                    cities_list.append(place)

            return cities_list
