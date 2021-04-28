import os
import json
import logging
from flask import request, current_app
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from snapsnare_api.system import responsify, tracer
from snapsnare_api.repositories.icecast_status.icecast_status_repository import IcecastStatusRepository


class CreateIcecastStatus(Resource):
    @jwt_required()
    def post(self):
        try:
            payload = request.get_json(silent=True)

            if not payload:
                return responsify(message='Invalid JSON content, or content-type header '
                                          'is not set to application/json'), 400

            connector = current_app.connector
            icecast_status_repository = IcecastStatusRepository(connector)

            source_ = {
                'source': json.dumps(payload.get('source'))
            }

            id_ = icecast_status_repository.insert(source_)
            icecast_status = icecast_status_repository.find_by(id=id_)

            connector.commit()
            connector.close()

            return responsify(uuid=icecast_status['uuid']), 200
        except Exception:
            response = tracer.build()
            logging.exception('create icecast_status failed')
            return response, 500


