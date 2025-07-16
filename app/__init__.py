from flask import Flask
from .routes.listener import listener_bp

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    app.register_blueprint(listener_bp)
    return app