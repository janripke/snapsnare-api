from uuid import uuid4

import click
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from paprika_connector.connectors.connector_factory import ConnectorFactory
from snapsnare_api.system import utils

from snapsnare_api.rest.auth.auth import Auth
from snapsnare_api.rest.properties.show_property import ShowProperty
from snapsnare_api.rest.jamulus.jammers import Jammers
from snapsnare_api.rest.jamulus.create_jammers import CreateJammers
from snapsnare_api.rest.icecast.create_icecast_status import CreateIcecastStatus
from snapsnare_api.templates.index.index import index

application = Flask(__name__)
api = Api(application)

ds = utils.load_json('snapsnare-ds.json')
connector = ConnectorFactory.create_connector(ds)
application.connector = connector

# set the secret, jwt uses this.
# every time the rest server start a new secret is created. Sessions do not survive a reboot.
application.config['SECRET_KEY'] = uuid4().hex

# initialize the logger
utils.load_logger('log.json', 'snapsnare-api')

# initialize jwt
application.config['JWT_SECRET_KEY'] = uuid4().hex
jwt = JWTManager(application)

api.add_resource(Auth, '/auth')
api.add_resource(ShowProperty, '/properties/show')
api.add_resource(Jammers, '/jamulus/jammers')
api.add_resource(CreateJammers, '/jamulus/jammers/create')
api.add_resource(CreateIcecastStatus, '/icecast/statuses/create')
application.register_blueprint(index)


@click.command()
@click.option('-d', '--debug', required=False, default=False, is_flag=True)
@click.option('-p', '--port', required=False, type=int, default=5001)
@click.option('-h', '--host', required=False, default='0.0.0.0')
def main(debug, port, host):
    application.run(debug=debug, port=port, host=host)


if __name__ == '__main__':
    main(args=None)
