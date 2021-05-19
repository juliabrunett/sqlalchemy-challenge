# Import flask dependencies
from flask import Flask, jsonify

# Import sqlalchemy & other dependencies
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
        "<strong><head>Welcome to the Climate App!</head></strong><br/><br/>"

        "<em><strong>Available Routes:</em></strong><br/>"

        "<p><em>Find precipitation data for the last year: </em><br/>"
        "/api/v1.0/precipitation</p>"

        "<p><em>Find station data: </em><br/>"
        "/api/v1.0/stations</p>"

        "<p><em>Find temperature data for the last year at the most active station: </em><br/>"
        "/api/v1.0/tobs</p>"

        "<p><em>Enter your own Start Date to see temperature statistics: </em><br/>"
        "/api/v1.0/2015-01-01</p>"

         "<p><em>Enter your own Start Date and End Date to see temperature statistics: </em><br/>"
        "/api/v1.0/2015-01-01/2016-01-01</p>" )

# Converts the query results from jupyter notebook exploration to a dictionary
# Returns the JSON representation of the dictionary
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
        prcp_dict[date] = precipitation
        precip.append(prcp_dict)

    return jsonify(precip)

# Returns a JSON list of stations from the dataset
@app.route("/api/v1.0/stations")
def stations():
    # Begin a session   
    session = Session(engine)

    # Query to find the most active stations 
    sel = [Station.id,
        Station.station,
        Station.name]

    # Create query that filters by the join between the tables
    stations_by_activity = session.query(*sel).filter(Station.station == Measurement.station).group_by(Station.id).order_by(Station.id).all()

    # Close the session
    session.close()

    # Create a list for station actvity
    station_activity = []

    # Loop through and create a dictionary and then append to the list
    for id, station, name in stations_by_activity:
        activity_dict = {}
        activity_dict["id"] = id
        activity_dict["station"] = station
        activity_dict["name"] = name
        station_activity.append(activity_dict)

    return jsonify(station_activity)

# Query the dates and temperature observations of the most active station
# Last year of data
@app.route("/api/v1.0/tobs")
def tobs():

     # Begin a session   
    session = Session(engine)

    # Retrieve the last 12 months of data for most active station
    sel = [Measurement.tobs,
        Measurement.date]

    # Query the last year of data for the most active station
    twelve_months_active = session.query(*sel).\
        filter(Measurement.date <= '2017-08-18').\
        filter(Measurement.date >= '2016-08-18').\
        filter(Measurement.station == "USC00519281").\
        order_by(Measurement.date).all()

    # Close the session
    session.close()

    #Create a list for the dictionary
    most_active_station = []

    # Loop through and create a dictionary and then append to the list
    for tobs, date in twelve_months_active:
        last_year_data = {}
        last_year_data["tobs"] = tobs
        last_year_data["date"] = date
        most_active_station.append(last_year_data)

    return jsonify(most_active_station)

# Returns a JSON list of the minimum, average, and max temperature for a given start date
@app.route("/api/v1.0/<start>")
def start(start):

     # Begin a session   
    session = Session(engine)

    # Retrieve the min, max, and average from a start date
    # What we will be selecting
    sel = [func.min(Measurement.tobs),
        func.max(Measurement.tobs),
        func.avg(Measurement.tobs)]

    # Query
    temperature_stats = session.query(*sel).filter(Measurement.date >= start)

    # Close the session
    session.close()

    # Create a list for the dictionary
    temp_stats = []

    # Loop through and create a dictionary and then append to the list
    for min_temp, max_temp, avg_temp in temperature_stats:
        stats = {}
        stats["min_temp"] = min_temp
        stats["max_temp"] = max_temp
        stats["avg_temp"] = avg_temp
        temp_stats.append(stats)

    return jsonify(temp_stats)

# Returns a JSON list of the minimum, average, and max temperature for a given start and end date
@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):

     # Begin a session   
    session = Session(engine)

    # Retrieve the min, max, and average from a start date
    # What we will be selecting
    sel = [func.min(Measurement.tobs),
        func.max(Measurement.tobs),
        func.avg(Measurement.tobs)]

    # Query
    temperature_stats = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end)

    # Close the session
    session.close()

     #Create a list for the dictionary
    temp_stats = []

    # Loop through and create a dictionary and then append to the list
    for min_temp, max_temp, avg_temp in temperature_stats:
        stats = {}
        stats["min_temp"] = min_temp
        stats["max_temp"] = max_temp
        stats["avg_temp"] = avg_temp
        temp_stats.append(stats)


    return jsonify(temp_stats)

# Debug app
if __name__ == "__main__":
    app.run(debug=True)
    
    
