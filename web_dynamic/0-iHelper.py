#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /hbnb_filters: HBnB HTML filters page.
"""
from models import storage
from models.city import City
from models.service import Service
import uuid
from flask import Flask, url_for, flash
from flask import render_template, request, redirect

from flask import flash
from werkzeug.utils import redirect
from flask_wtf import FlaskForm



app = Flask(__name__)


@app.route("/iHelper", strict_slashes=False)
def iHelper():
    """Displays the main HBnB filters HTML page."""
    states = storage.all(City)
    amenities = storage.all(Service)
    return render_template("helper0.html",
                           states=states, amenities=amenities, cache_id=uuid.uuid4())

# @app.route("/iHelper/signup", strict_slashes=False)
# def iHelper_signup():
#     """Displays the main HBnB filters HTML page."""
#     states = storage.all(City)
#     amenities = storage.all(Service)
#     return render_template("signup.html",
#                            states=states, amenities=amenities, cache_id=uuid.uuid4())

@app.route("/iHelper/service", strict_slashes=False)
def iHelper_service():
    """Displays the main HBnB filters HTML page."""
    states = storage.all(City)
    amenities = storage.all(Service)
    return render_template("service.html",
                           states=states, amenities=amenities, cache_id=uuid.uuid4())

@app.route("/iHelper/signin", strict_slashes=False)
def iHelper_signin():
    """Displays the main HBnB filters HTML page."""
    states = storage.all(City)
    amenities = storage.all(Service)
    return render_template("signin.html",
                           states=states, amenities=amenities, cache_id=uuid.uuid4())


@app.route("/iHelper/search", strict_slashes=False)
def iHelper_search():
    """Displays the main HBnB filters HTML page."""
    states = storage.all(City)
    amenities = storage.all(Service)
    city = request.args.get('city')
    amenities = request.args.get('amenities').split(',')
    return render_template("search.html",
                           states=states, amenities=amenities, city=city, cache_id=uuid.uuid4())

# Price page
@app.route("/iHelper/price", methods=["GET"])
def price():
    city = request.args.get("city")
    amenities_str = request.args.get("amenities")
    amenities = amenities_str.split(",") if amenities_str else []
    appointment = request.args.get("appointment")
    task = request.args.get("task")
    task_size = request.args.get("task-size")

    # Calculate price based on the transferred values
    # price = calculate_price(city, amenities, appointment, task, task_size)
    # price = calculate_price(city, amenities, appointment, task, task_size)
     # Get all instances of Service class from database
    services = storage.all(Service)
  
    


    # Calculate total price for selected tasks and amenities based on task size
    total_price = 0
    for selected_amenity in amenities:
        print(selected_amenity)
        for service in services.values():
            print(service)
            if service.name == selected_amenity:
                print(service.name)
                amenity_price = service.price
                if task_size == 'small':
                    amenity_price *= 2
                elif task_size == 'medium':
                    amenity_price *= 3
                else:
                    amenity_price *= 4
                total_price += amenity_price


    return render_template("price.html", city=city, amenities=amenities, appointment=appointment, task=task, task_size=task_size, total_price=total_price, services=services)


@app.route("/iHelper/about_us", strict_slashes=False)
def iHelper_about():
    """Displays the main HBnB filters HTML page."""
    # states = storage.all(City)
    # amenities = storage.all(Service)
    # city = request.args.get('city')
    # amenities = request.args.get('amenities').split(',')
    return render_template("aboutas.html",
                            cache_id=uuid.uuid4())





from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from models.user import User
from models import DBStorage

app.config['SECRET_KEY'] = 'supersecretkey'
db_storage = DBStorage()

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=128)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=128)])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), Length(min=8, max=128)])
    first_name = StringField('First Name', validators=[InputRequired(), Length(max=128)])
    last_name = StringField('Last Name', validators=[InputRequired(), Length(max=128)])
    phone_number = StringField('Phone Number', validators=[InputRequired(), Length(max=128)])
    terms_and_conditions = BooleanField('I agree to the terms and conditions', validators=[InputRequired()])
    submit = SubmitField('Sign Up')

@app.route('/iHelper/signup', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.password.data != form.confirm_password.data:
            flash('Passwords do not match')
            return redirect(url_for('register'))
        user = User(
            email=form.email.data,
            password=form.password.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            phone_number=form.phone_number.data
        )
        db_storage.new(user)
        db_storage.save()
        return redirect(url_for('success'))
    return render_template('signup.html', form=form, cache_id=uuid.uuid4())

@app.route('/success')
def success():
    return 'Account created successfully!'






if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)

   
