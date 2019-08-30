from flask import Blueprint, request
from flask_restplus import Api, Resource
from flask_jwt_extended import create_access_token, create_refresh_token

from DB import curs

api = Api(Blueprint(__name__, __name__))


@api.route('/signin')
class Signin(Resource):
    def post(self):
        try:
            tell = request.json['tell']
            pw = request.json['pw']
        except KeyError or TypeError:
            return {'msg': 'value_skipped'}, 400

        query_select_user_info = 'select tell, pw, uuid from user where tell = %s and pw = %s'
        curs.execute(query_select_user_info, (tell, pw))
        existing_user_info = curs.fetchone()

        if not existing_user_info:
            return {'msg': 'invalid_info'}, 401

        identity = {'uuid': existing_user_info['uuid']}

        return {'access_token': create_access_token(identity=identity),
                'refresh_token': create_refresh_token(identity=identity)}, 200
