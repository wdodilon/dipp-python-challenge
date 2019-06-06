"""
Scripts
"""
from flask_script import Manager
from flask import current_app
from app import create_app

def create_my_app():
    """
    Method to create the Flask application
    """
    app = create_app()
    return app

APP = create_my_app()
manager = Manager(APP)

@manager.command
def run():
    """
    Command to run the API locally.
    """
    port = int(current_app.config['PORT'])
    host = current_app.config['HOST']
    debug = current_app.config['DEBUG']
    current_app.run(host=host, port=port, debug=debug)

@manager.command
def make_image():
    """
    Command to make the API request and use the output to create an image
    """
    payload = {
        "facebook-header": {
            "copy": "dipp inc, thinking out of the box.",
            "x_start": 250,
            "y_start": 250,
            "max_width": 200,
            "max_height": 200,
            "font_url": "https://fonts.gstatic.com/s/cinzeldecorative/v7/daaHSScvJGqLYhG8nNt8KPPswUAPniZQa-lDQzCLlQXE.ttf"
        }
    }

    dimensions = (700, 700)

    # Please insert your code here

if __name__ == "__main__":
    manager.run()
