# Import flask dependencies
from flask import Flask, jsonify

# Setup the flask app
app = Flask(__name__)

# Create a flask route for home
@app.route("/")
def home():
    print("Opening message")
    return "Home Page"

# Create a flask route for returning json
@app.route("/jsonified")
def jsonified():
    return jsonify()

# Debug app
if __name__ == "__main__":
    app.run(depug=True)
    
    
