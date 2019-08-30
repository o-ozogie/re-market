from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from views.route import Route


def create_app(*configs):
    app_ = Flask(__name__)

    for config in configs:
        app_.config.from_object(config)

    CORS(app_, resources={
        r"*": {'origin': '*'},
    })

    JWTManager().init_app(app_)
    Route().route(app_)

    return app_
