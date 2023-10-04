# import Python modules
from dotenv import load_dotenv
from flask import Flask
from os import environ

#---------------------------------------------------------------------#

# create Flask app
app = Flask(__name__)

# Load environment variables
load_dotenv()

# Create secret key to use Flask session feature
app.secret_key = environ['APPSECRETKEY']

# Make the Flask interactive debugger better in testing 
# TODO - remove before deployment
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True

#---------------------------------------------------------------------#

@app.route("/test")
def index():
    """Return test."""
    print("Testing Successful")
    return 'Successful Test'

#---------------------------------------------------------------------#

# when this file is run
if __name__ == "__main__":
    # run server
    app.run(debug=True, host="0.0.0.0")

