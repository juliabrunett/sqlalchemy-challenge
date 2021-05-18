# Import flask dependencies
from flask import Flask, jsonify

# Import sqlalchemy dependencies
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Build engine and base
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save a reference to the 2 classes
Station = Base.classes.station
Measurement = Base.classes.measurement

# Setup the flask app
app = Flask(__name__)

# Create a flask route for home
@app.route("/")
def home():
    return (
        "Welcome to my Home Page!<br/>"
        "Available Routes:<br/>"
        "/api/v1.0/precipitation<br/>"
        "/api/v1.0/stations<br/>"
        "/api/v1.0/tobs<br/>"
        "/api/v1.0/<start><br/>"
        "/api/v1.0/<start>/<end><br/>" )

# Create a flask route for returning json
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Begin a session
    session = Session(engine)

    # define selections
    sel = [Measurement.date,
       func.sum(Measurement.prcp)]

    # Retrieve the last 12 months of precipitation data
    twelve_months = session.query(*sel).\
        filter(Measurement.date <= '2017-08-23').\
        filter(Measurement.date >= '2016-08-23').\
        order_by(Measurement.date).group_by(Measurement.date).all()

    # Close the session
    session.close()

    # Create a precipitation list
    precip = []

    # Loop through and create a dictionary and then append to the list
    for date, precipitation in twelve_months:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["precipitation"] = precipitation
        precip.append(prcp_dict)

    return jsonify(precip)

@app.route("/api/v1.0/stations")
def stations():
    # Begin a session   
    session = Session(engine)

    # Query to find the most active stations 
    sel = [Station.id,
        Station.station,
        Station.name,
        func.count(Measurement.id)]

    # Create query that filters by the join between the tables
    stations_by_activity = session.query(*sel).filter(Station.station == Measurement.station).\
        group_by(Station.id).order_by(func.count(Measurement.id).desc()).all()

    # Close the session
    session.close()

    # Create a list for station actvity
    station_activity = []

    # Loop through and create a dictionary and then append to the list
    for id, station, name, measurement_id_count in stations_by_activity:
        activity_dict = {}
        activity_dict["id"] = id
        activity_dict["station"] = station
        activity_dict["name"] = name
        activity_dict["measurement_id_count"] = measurement_id_count
        station_activity.append(activity_dict)

    return jsonify(station_activity)

@app.route("/api/v1.0/tobs")
def tobs():
    return jsonify()

@app.route("/api/v1.0/<start>")
def start():

    return jsonify()

@app.route("/api/v1.0/<start>/<end>")
def start_end():
    return jsonify()

# Debug app
if __name__ == "__main__":
    app.run(debug=True)
    
    
