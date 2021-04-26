import os
import logging
from flask import request, current_app, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from snapsnare_api.system import responsify, tracer
from snapsnare_api.repositories.property.property_repository import PropertyRepository
from snapsnare_api.system import utils


class Jammers(Resource):
    @jwt_required()
    def get(self):
        try:

            jammers = utils.load(os.path.join('/opt', 'jamulus', 'status'))
            print(jammers)
            return responsify(jammers=jammers), 200
        except Exception:
            response = tracer.build()
            logging.exception('show property failed')
            return response, 500


