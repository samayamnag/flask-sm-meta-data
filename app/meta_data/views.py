from . import meta_data_blueprint

from flask.views import MethodView
from flask import make_response, jsonify
from .models import State
from .services.state_service import get_states, get_districts, get_cities, get_civic_agencies
from app.utils import get_locale


class StateView(MethodView):

    def get(self):
        response = get_states()
        if "data" in response:
            return make_response(jsonify(
                data=response['data'],
                language=get_locale(),
                links=response['links'],
                meta=response['meta']
            ))

        return make_response(jsonify({'message': 'No records found'})), 404

    
class DistrictView(MethodView):

    def get(self):
        response = get_districts()
        if "data" in response:
            return make_response(jsonify(
                data=response['data'],
                language=get_locale(),
                links=response['links'],
                meta=response['meta']
            ))

        return make_response(jsonify({'message': 'No records found'})), 404


class CityView(MethodView):

    def get(self):
        response = get_cities()
        if "data" in response:
            return make_response(jsonify(
                data=response['data'],
                language=get_locale(),
                links=response['links'],
                meta=response['meta']
            ))

        return make_response(jsonify({'message': 'No records found'})), 404


class CivicAgencyView(MethodView):

    def get(self):
        response = get_civic_agencies()
        if "data" in response:
            return make_response(jsonify(
                data=response['data'],
                language=get_locale(),
                links=response['links'],
                meta=response['meta']
            ))

        return make_response(jsonify({'message': 'No records found'})), 404



# Define the API resource
state_view = StateView.as_view('state_view')
district_view = DistrictView.as_view('district_view')
city_view = CityView.as_view('city_view')
civic_agency_view = CivicAgencyView.as_view('civic_agency_view')


# Add the url rule for registering
meta_data_blueprint.add_url_rule(
    '/states',
    view_func=state_view,
    methods=['GET'])
meta_data_blueprint.add_url_rule(
    '/districts',
    view_func=district_view,
    methods=['GET'])
meta_data_blueprint.add_url_rule(
    '/cities',
    view_func=city_view,
    methods=['GET'])
meta_data_blueprint.add_url_rule(
    '/civic-agencies',
    view_func=civic_agency_view,
    methods=['GET'])
