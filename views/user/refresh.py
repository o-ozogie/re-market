from flask import Blueprint
from flask_restplus import Api, Resource
from flask_jwt_extended import jwt_refresh_token_required, get_jwt_identity, create_access_token

api = Api(Blueprint(__name__, __name__))


@api.route('/refresh')
class Refresh(Resource):
    @jwt_refresh_token_required
    def get(self):
        identity = get_jwt_identity()
        return {'access_token': create_access_token(identity=identity)}, 200
