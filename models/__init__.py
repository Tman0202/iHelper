#!/usr/bin/python3
"""Create a unique storage instance for your application"""

from os import environ
from models.main_models import MainModel
from models.user import User
from models.request import Request
from models.city import City
from models.payment import Payment
from models.place import Place
from models.review import Review
from models.service import Service

# check envirn var to determine storage method
if environ['IHELPER_TYPE_STORAGE'] == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()

else:  # file storage selected
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()