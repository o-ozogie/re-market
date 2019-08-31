from flask import Blueprint, request
from flask_restplus import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from DB import conn, curs

api = Api(Blueprint(__name__, __name__))


@api.route('/upload')
class Upload(Resource):
    @jwt_required
    def post(self):
        try:
            title = request.json['title']
            content = request.json['content']
            main_img = request.json['main_img']
            price = request.json['price']
            cate = request.json['cate']
        except KeyError or TypeError:
            return {'msg': 'value_skipped'}, 400

        try:
            desired_item = request.json['desired_item']
        except KeyError or TypeError:
            desired_item = None

        identity = get_jwt_identity()

        query_insert_item = 'insert into item (user, title, content, cate, main_img, price, desired_item, write_time)' \
                            ' values (%s, %s, %s, %s, %s, %s, %s, now())'
        curs.execute(query_insert_item, (identity['uuid'], title, content, cate, main_img, price, desired_item))
        conn.commit()

        return {'msg': 'success'}, 200
