#Import Dependencies
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import os

file_path = os.path.abspath(os.getcwd())+"/Unit 9 - SQLAlchemy/Resources/hawaii.sqlite"

#Databse Setup
engine = create_engine("sqlite:///" + file_path)

#Reflect
Base = automap_base()
Base.prepare(engine, reflect=True)

#Save reference to the table
measurement = Base.classes.measurement
station = Base.classes.station


#flask setup
app = Flask(__name__)

@app.route("/")
def homepage():
    return(
        f"Available Routes:<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    results = session.query(measurement.date, measurement.prcp).\
                order_by(measurement.date).all()
    
    precipitation_list = []

    for date, prcp in results:
        new_dict = {}
        new_dict[date] = prcp
        precipitation_list.append(new_dict)
    
    session.close()

    return jsonify(precipitation_list)


@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    stations = {}

    results = session.query(station.station, station.name).all()

    for s, name in results:
        stations[s] = name
    
    session.close()

    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    last_date = session.query(measurement.date).order_by(measurement.date.desc()).first()
    one_year = (dt.datetime.strptime(last_date[0],'%Y-%m-%d') \
                    - dt.timedelta(days=365)).strftime('%Y-%m-%d')
    
    results = session.query(measurement.date, measurement.tobs).\
                filter(measurement.date >= one_year).\
                order_by(measurement.date).all()
    
    tobs_list = []

    for date, tobs in results:
        new_dict = {}
        new_dict[date] = tobs
        tobs_list.append(new_dict)
    
    session.close()

    return jsonify(tobs_list)


@app.route("/api/v1.0/<start>")
def temp_range_start(start):
    session = Session(engine)

    return_list = []

    results = session.query(measurement.date,
                            func.min(measurement.tobs),\
                            func.avg(measurement.tobs),\
                            func.max(measurement.tobs)).\
                            filter(measurement.date >= start).\
                            group_by(measurement.date).all()

    for date, min, avg, max in results:
        new_dict = {}
        new_dict["Date"] = date
        new_dict["TMIN"] = min
        new_dict["TAVG"] = avg
        new_dict["TMAX"] = max
        return_list.append(new_dict)

    session.close()    

    return jsonify(return_list)


@app.route("/api/v1.0/temperature/<start>/<end>")
def temperature(start=None,end=None):
    session = Session(engine)

    return_list = []

    results = session.query(measurement.date,
                            func.min(measurement.tobs),\
                            func.avg(measurement.tobs),\
                            func.max(measurement.tobs)).\
                            filter(measurement.date >= start).filter(measurement.date <= end).\
                            group_by(measurement.date).all()

    for date, min, avg, max in results:
        dict = {}
        dict["Date"] = date
        dict["TMIN"] = min
        dict["TAVG"] = avg
        dict["TMAX"] = max
        return_list.append(dict)

    session.close()    

    return jsonify(return_list)

if __name__ == '__main__':
    app.run()
