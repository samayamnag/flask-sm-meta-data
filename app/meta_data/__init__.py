from flask import Blueprint


meta_data_blueprint = Blueprint('data', '__name__')

from . import views
