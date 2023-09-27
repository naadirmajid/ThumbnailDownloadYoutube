# Import necessary modules
from flask import Flask, render_template, request
from your_flask_app_file import app as flask_app  # Assuming your Flask app is named 'app' and it's in 'your_flask_app_file.py'

# Create the WSGI application object
app = flask_app

# If the file is executed, run the Flask development server
if __name__ == "__main__":
    app.run()
