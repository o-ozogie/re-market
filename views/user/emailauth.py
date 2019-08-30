from flask import Blueprint, request
from flask_restplus import Api, Resource

from DB import curs, conn
from config.const import BASIC_PROFILE_IMAGE

api = Api(Blueprint(__name__, __name__))


@api.route('/emailauth')
class EmailAuth(Resource):
    def post(self):
        try:
            cert_num = request.json['cert_num']
            inserted_num = request.json['inserted_num']
            tell = request.json['tell']
            pw = request.json['pw']
            name = request.json['name']
            email = request.json['email']
            permission = request.json['permission']
            zone_code = request.json['zone_code']
            address = request.json['address']
            detail_address = request.json['detail_address']
            profile_img = BASIC_PROFILE_IMAGE
        except KeyError or TypeError:
            return {'msg': 'value_permission'}, 400

        if cert_num != inserted_num:
            return {'msg': 'invalid_cert_num'}, 495

        query_insert_user_info = 'insert into user (tell, pw, name, email, permission, zonecode, address, detailaddress, profileimg)' \
                                 ' values (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        curs.execute(query_insert_user_info,
                     (tell, pw, name, email, permission, zone_code, address, detail_address, profile_img))
        conn.commit()

        return {'msg': 'success'}, 200
