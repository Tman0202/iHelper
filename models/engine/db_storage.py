#!/usr/bin/python3
"""Define storage engine using MySQL database
"""
from models.main_models import MainModel, Base
from models.user import User
from models.service import Service
from models.city import City
from models.request import Request
from models.place import Place
from models.review import Review
from models.payment import Payment
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import sessionmaker, Session
from os import getenv
import models

all_classes = { 'City': City,
                'Place': Place, 'User': User, 'Review': Review,
                'Payment': Payment, 'Service': Service }


class DBStorage:
    """This class manages MySQL storage using SQLAlchemy
    Attributes:
        __engine: engine object
        __session: session object
    """
    __engine = None
    __session = None

    def __init__(self):
        """Create SQLAlchemy engine
        """
        # create engine
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(getenv('IHELPER_MYSQL_USER'),
                                             getenv('IHELPER_MYSQL_PWD'),
                                             getenv('IHELPER_MYSQL_HOST'),
                                             getenv('IHELPER_MYSQL_DB')),
                                      pool_pre_ping=True)
        # drop tables if test environment
        if getenv('IHELPER_ENV') == 'test':
                Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query and return all objects by class/generally
        Return: dictionary (<class-name>.<object-id>: <obj>)
        """
        obj_dict = {}

        if cls:
            for row in self.__session.query(cls).all():
                # populate dict with objects from storage
                obj_dict.update({'{}.{}'.
                                format(type(cls).__name__, row.id,): row})
        else:
            for key, val in all_classes.items():
                for row in self.__session.query(val):
                    obj_dict.update({'{}.{}'.
                                    format(type(row).__name__, row.id,): row})
        return obj_dict

    def new(self, obj):
        """Add object to current database session
        """
        self.__session.add(obj)

    def save(self):
        """Commit current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from database session
        """
        if obj:
            # determine class from obj
            cls_name = all_classes[type(obj).__name__]

            # query class table and delete
            self.__session.query(cls_name).\
                filter(cls_name.id == obj.id).delete()

    def reload(self):
        """Create database session
        """
        # create session from current engine
        Base.metadata.create_all(self.__engine)
        # create db tables
        session = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        # previousy:
        # Session = scoped_session(session)
        self.__session = scoped_session(session)

    def close(self):
        """Close scoped session
        """
        self.__session.remove()

    def get(self, cls, id):
        """ Method to retrieve an object with specified id """
        if cls in all_classes.values():
            for obj in models.storage.all(cls).values():
                if obj.id == id:
                    return obj
        return None

    def count(self, cls=None):
        """ Method to count the number of objects in
            the current database session or specified table
        """
        if (cls is not None) and (cls in all_classes.values()):
            count = len(models.storage.all(cls).values())
        elif (cls is not None) and (cls not in all_classes.values()):
            return 0
        else:
            count = 0
            for obj in all_classes.values():
                count += len(models.storage.all(obj).values())
        return count    