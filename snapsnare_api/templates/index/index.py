from flask import Blueprint, render_template
from flask import request, current_app
import snapsnare_api
from snapsnare_api.repositories.property.property_repository import PropertyRepository

index = Blueprint('index', __name__, template_folder='templates')


@index.route('/')
def show():
    if request.method == 'GET':

        connector = current_app.connector
        property_repository = PropertyRepository(connector)
        properties_ = property_repository.list_by()

        code = {
            'name': snapsnare_api.__name__,
            'version': snapsnare_api.__version__,
        }

        return render_template('index/index.html', code=code, properties=properties_)
