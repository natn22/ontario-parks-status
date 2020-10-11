from flask import Flask

def create_app():
    app = Flask(__name__)
    from src.api.campsite.controllers import campsite
    app.url_map.strict_slashes = False
    app.register_blueprint(campsite, url_prefix='/api')
    return app