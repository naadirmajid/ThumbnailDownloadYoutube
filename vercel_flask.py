from youtube_thumbnail_webapp import app as flask_app  # Replace 'your_flask_app_file' with your actual Flask app file's name

def app(environ, start_response):
    return flask_app(environ, start_response)
