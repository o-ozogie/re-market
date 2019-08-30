from flask import Blueprint, request
from flask_restplus import Api, Resource

from DB import curs

api = Api(Blueprint(__name__, __name__))

@api.route('/mainpage')
class Mainpage(Resource):
    def get(self):
        try:
            address = request.args['address']
        except KeyError or TypeError:
            return {'msg': 'value_skipped'}, 400

        query_select_user_uuid = 'select uuid, name from user where address = %s'
        curs.execute(query_select_user_uuid, address)
        users = curs.fetchall()

        refined_info = {}

        cnt = 0
        for user in users:
            query_select_item_info = 'select uuid, title, main_img, price, desired_item, write_time ' \
                                     'from item where user = %s order by write_time desc'

            curs.execute(query_select_item_info, user['uuid'])
            items = curs.fetchall()
            for item in items:
                item['write_time'] = item['write_time'].strftime('%Y-%m-%d:%H:%M:%S')
                item['name'] = user['name']
                refined_info[cnt] = item
                cnt += 1

        return refined_info, 200
