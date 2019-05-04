import numpy as np

from datetime import datetime

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

## Database ##

# Need to set 'check_same_thread' argument to avoid threading errors 
engine = create_engine("sqlite:///hawaii.sqlite",connect_args={'check_same_thread': False})

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

## Flask ##

app = Flask(__name__)

@app.route("/")
def welcome():
    """List of api routes"""
    return (
        f"Available routes on /api/v1.0/*:<br/>"
        f"precipitation<br/>"
        f"stations<br/>"
        f"tobs<br/>"
        f"start_day (YYYY-MM-DD)"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """ Query for the dates and precipitation observations """
    """ Convert the results to a dictionary and return the JSON representation """
    results = session.query(Measurement).all()
    all_measurements = []
    for measurement in results:
        measurement_dict = {}
        measurement_dict["date"] = measurement.date
        measurement_dict["prcp"] = measurement.prcp
        all_measurements.append(measurement_dict)
    return jsonify(all_measurements)

@app.route("/api/v1.0/stations")
def stations():
    """ Return a JSON list of stations """
    results = session.query(Station.name).all()
    station_names = list(np.ravel(results))
    return jsonify(station_names)

@app.route("/api/v1.0/tobs")
def tobs():
    """ Query for the dates and temperature observations from a year from the last data point """
    """ Return a JSON list of that query """
    q = session.query(Measurement.date)
    last = q.order_by(Measurement.date.desc()).first()
    lastday = datetime.strptime(last[0],'%Y-%m-%d').date()
    startday = lastday.replace(lastday.year-1)
    results = session.query(Measurement).filter(Measurement.date>=startday).all()
    temps = []
    for result in results:
        t_dict = {}
        t_dict["date"] = result.date
        t_dict["tobs"] = result.tobs
        temps.append(t_dict)
    return jsonify(temps)

@app.route("/api/v1.0/<start_date>")
def tobs_start(start_date):
    startday = datetime.strptime(start_date,'%Y-%m-%d').date()
    results = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).\
        filter(Measurement.date>=startday).all()
    t_stats = list(np.ravel(results))
    return jsonify(t_stats)

if __name__ == '__main__':
    app.run(debug=True)