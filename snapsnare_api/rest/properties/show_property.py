import logging
from flask import request, current_app, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from snapsnare_api.system import responsify, tracer
from snapsnare_api.repositories.property.property_repository import PropertyRepository


class ShowProperty(Resource):
    @jwt_required()
    def get(self):
        try:
            connector = current_app.connector

            name = request.args.get('name')

            if not name:
                return jsonify(message='property name is required'), 400

            property_repository = PropertyRepository(connector)
            property_ = property_repository.find_by_name(name)
            print(property_)
            logging.debug(property_)

            if not property_:
                return jsonify(message='property not found'), 404

            return responsify(property=property_), 200
        except Exception:
            response = tracer.build()
            logging.exception('show property failed')
            return response, 500


