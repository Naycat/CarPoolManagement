

from flask import Flask, request, jsonify, make_response, render_template, abort  # pylint: disable=unused-import # type: ignore
from flask_sqlalchemy import SQLAlchemy  # pylint: disable=unused-import # type: ignore
# from marshmallow_sqlalchemy import ModelSchema
# from marshmallow import fields
from sqlalchemy.ext.automap import automap_base  # pylint: disable=unused-import # type: ignore
from sqlalchemy.orm import Session  # pylint: disable=unused-import # type: ignore
from sqlalchemy import create_engine  # pylint: disable=unused-import disable=import-error# type: ignore
# from data import AllCars, CarPool, Booking, Drivers  # pylint: disable=unused-import # type: ignore
import datetime
# from wtforms_sqlalchemy.fields import QuerySelectField
# from flask_wtf import FlaskForm
# pylint: enable=no-member


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://app:appass@127.0.0.1:3306/carPoolDB'
db = SQLAlchemy(app)


# allCarOptions = db.Table("allCarOptions", db.metadata,
#                          autoload=True, autoload_with=db.engine)
# carPool = db.Table("carPool", db.metadata, autoload=True,
#                    autoload_with=db.engine)
# drivers = db.Table("drivers", db.metadata, autoload=True,
#                    autoload_with=db.engine)
# reservations = db.Table("reservations", db.metadata,
# autoload = True, autoload_with = db.engine)

Base = automap_base()

engine = create_engine("mysql+pymysql://app:appass@127.0.0.1:3306/carPoolDB")

Base.prepare(engine, reflect=True, schema='carPoolDB')
AllCars = Base.classes.allCarOptions
CarPool = Base.classes.carPool
Booking = Base.classes.reservations
Drivers = Base.classes.drivers


@ app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@ app.errorhandler(500)
def page_not_found(error):
    return render_template('500.html'), 500


@ app.route('/500')
def error500():
    abort(500)


@ app.route('/')
@ app.route('/index')
def index():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())


@ app.route('/all_cars', methods=['GET'])
def all_cars():

    cars = db.session.query(AllCars).all()
    return render_template('all_cars_table.html', title='Car Inventory',
                           cars=cars)


@ app.route('/list_cars', methods=['GET'])
def list_cars():
    a_cars_list = db.session.query(CarPool).all()
    join = db.session.query(CarPool, AllCars).filter(
        CarPool.idCar == AllCars.car_id).all()
    return render_template('list_cars.html', title='Car Availability',
                           a_cars_list=a_cars_list, join=join)


@ app.route('/add_car', methods=['GET'])
def add_car():
    pass
#     # form.opts.query = Choice.query.filter(Choice.id > 1)
#     if form.validate_on_submit():
#         return '<html><h1>{}</h1></html>'.format(form.opts.data)
#     return render_template('index.html', form=form)
#     return render_template('add_car.html', title='add car to available')


@ app.route('/car_detail', methods=['GET'])
def car_detail():
    # cars = AllCars.query
    # return render_template('cardetail.html', title='Car Inventory',
    #                        cars=cars)
    pass


@ app.route('/deletecar', methods=['GET'])
def delcar():
    # cars = .query
    # return render_template('all_cars_table.html', title='Car Inventory',
    #                        cars=cars)
    pass


@ app.route('/book_a_car')
def book_a_car():
    pass


@ app.route('/bookings_history_table')
def bookings():
    pass

# @app.route('/allcars', methods = ['GET'])
# def index():
#     get_cars = AllCars.query.all()
#     cars_schema = AllCars.metadata.schema
#     cars = cars_schema.dump(get_cars)
#     return render_template('allcars.html', cars=cars)


def choice_query():
    return AllCars.query


# class add_car_Form(FlaskForm):
#     opts = QuerySelectField(query_factory=choice_query,
#                             allow_blank=False, get_label='name')
