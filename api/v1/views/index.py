#!/usr/bin/python3
""" Index """
from models.service import Service
from models.city import City
from models.place import Place
from models.review import Review
from models.payment import Payment
from models.user import User
from models.request import Request
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    classes = [Request, City, Place, Review, Payment, User, Service]
    names = ["Requests", "cities", "places", "reviews","Payments", "users", "services"]

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)
