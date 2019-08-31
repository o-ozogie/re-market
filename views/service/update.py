from flask import Blueprint, request
from flask_restplus import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from DB import curs, conn

api = Api(Blueprint(__name__, __name__))


@api.route('/update')
class Update(Resource):
    @jwt_required
    def patch(self):
        try:
            uuid = request.json['uuid']
            status = request.json['status']
        except KeyError or TypeError:
            return {'msg': 'value_skipped'}, 400

        query_update_item_info = 'update item set status = %s where uuid = %s'
        curs.execute(query_update_item_info, (status, uuid))
        conn.commit()

        return {'msg': 'success'}, 200

    @jwt_required
    def delete(self):
        identity = get_jwt_identity()

        try:
            uuid = request.json['uuid']
        except KeyError or TypeError:
            return {'msg': 'value_skipped'}, 400

        query_delete_item_info = 'delete from item where user = %s and uuid = %s'
        curs.execute(query_delete_item_info, (identity['uuid'], uuid))
        conn.commit()

        return {'msg': 'success'}, 200
