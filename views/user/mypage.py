from flask import Blueprint, request
from flask_restplus import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from DB import curs, conn

api = Api(Blueprint(__name__, __name__))


@api.route('/mypage')
class Mypage(Resource):
    @jwt_required
    def get(self):
        identity = get_jwt_identity()

        query_select_user_info = 'select tell, name, email, zonecode, address, detailaddress from user where uuid = %s'
        curs.execute(query_select_user_info, identity['uuid'])
        existing_user_info = curs.fetchone()

        query_select_item_info = 'select '

        return existing_user_info

    @jwt_required
    def patch(self):
        identity = get_jwt_identity()

        try:
            pw = request.json['pw']
        except KeyError or TypeError:
            return {'msg': 'value_skipped'}, 400
        try:
            change_pw = request.json['change_pw']
        except KeyError or TypeError:
            change_pw = None
        try:
            name = request.json['name']
        except KeyError or TypeError:
            name = None
        try:
            profile_img = request.json['profile_img']
        except KeyError or TypeError:
            profile_img = None

        query_select_info = 'select pw from user where pw = %s'
        curs.execute(query_select_info, pw)
        present_pw = curs.fetchone()
        if not present_pw:
            return {'msg': 'pw_incorrect'}, 401

        if change_pw:
            query_update_info = 'update user set pw = %s where uuid = %s'
            curs.execute(query_update_info, (change_pw, identity['uuid']))

        if name:
            query_update_info = 'update user set name = %s where uuid = %s'
            curs.execute(query_update_info, (name, identity['uuid']))

        if profile_img:
            query_update_info = 'update user set profileimg = %s where uuid = %s'
            curs.execute(query_update_info, (profile_img, identity['uuid']))

        conn.commit()
        return {'msg': 'success'}, 200
