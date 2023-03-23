#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.cities import *
# from iHelper.api.v1.views.payments import *
from api.v1.views.places_reviews import *
# from iHelper.api.v1.views.places import *
# from iHelper.api.v1.views.services import *
from api.v1.views.users import *
from api.v1.views.places_amenities import *
