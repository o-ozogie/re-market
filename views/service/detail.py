from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from flask_restplus import Api, Resource

from DB import curs

api = Api(Blueprint(__name__, __name__))


@api.route('/detail')
class Detail(Resource):
    @jwt_required
    def get(self):
        try:
            item_uuid = request.args['uuid']
        except KeyError or TypeError:
            return {'msg': 'not_json'}, 406

        query_select_item = 'select title, content, main_img, price, desired_item, write_time ' \
                            'from item where uuid = %s'
        curs.execute(query_select_item, item_uuid)
        detail_item = curs.fetchone()

        refined_detail_item = detail_item
        return refined_detail_item, 200
