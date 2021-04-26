import os
import logging
from flask import request, current_app
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from snapsnare_api.system import responsify, tracer
from snapsnare_api.repositories.jammer.jammer_repository import JammerRepository


class CreateJammers(Resource):
    @jwt_required()
    def post(self):
        try:
            payload = request.get_json(silent=True)

            if not payload:
                return responsify(message='Invalid JSON content, or content-type header '
                                          'is not set to application/json'), 400

            connector = current_app.connector
            jammer_repository = JammerRepository(connector)

            jammers_ = {
                'jammers': payload.get('jammers')
            }

            jammer_id = jammer_repository.insert(jammers_)
            jammers = jammer_repository.find_by(id=jammer_id)

            connector.commit()
            connector.close()

            return responsify(uuid=jammers['uuid']), 200
        except Exception:
            response = tracer.build()
            logging.exception('create jammers failed')
            return response, 500


