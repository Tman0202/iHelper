#!/usr/bin/python3
""" objects that handles all default RestFul API actions for cities """
from models.city import City
from models.place import Place
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/cities/<city_id>/places', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/city/cities_by_state.yml', methods=['GET'])
def get_cities(city_id):
    """
    Retrieves the list of all cities objects
    of a specific State, or a specific city
    """
    print(city_id)
    list_cities = []
    city = storage.get(City, city_id)
    print("city")
    if not city:
        abort(404)
    for place in city.places:
        list_cities.append(place.to_dict())

    return jsonify(list_cities)


@app_views.route('/places/<place_id>/', methods=['GET'], strict_slashes=False)
@swag_from('documentation/city/get_city.yml', methods=['GET'])
def get_city(place_id):
    """
    Retrieves a specific city based on id
    """
    city = storage.get(City, place_id)
    if not city:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/city/delete_city.yml', methods=['DELETE'])
def delete_city(place_id):
    """
    Deletes a city based on id provided
    """
    city = storage.get(Place, place_id)

    if not city:
        abort(404)
    storage.delete(city)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/cities/<city_id>/cities', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/city/post_city.yml', methods=['POST'])
def post_city(city_id):
    """
    Creates a City
    """
    state = storage.get(City, city_id)
    if not state:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = Place(**data)
    instance.city_id = state.id
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/city/put_city.yml', methods=['PUT'])
def put_city(place_id):
    """
    Updates a City
    """
    city = storage.get(Place, place_id)
    if not city:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'state_id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(city, key, value)
    storage.save()
    return make_response(jsonify(city.to_dict()), 200)