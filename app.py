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

# Begin a session
session = Session(engine)

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
        "/api/v1.0/<start>/<end><br/>"

# Create a flask route for returning json
@app.route("/api/v1.0/precipitation")
def precipitation():
    {date: prcp}
    return jsonify()

@app.route("/api/v1.0/stations")
def stations():
    {stations}
    return jsonify()

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
    app.run(depug=True)
    
    
