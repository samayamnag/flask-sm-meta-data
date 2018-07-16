from . import meta_data_blueprint

from flask.views import MethodView
from flask import make_response, jsonify
from .models import State
from app.utils import (
    get_locale, per_page, page_num,
    pagination_meta_data, pagination_links
)


class StateView(MethodView):

    def get(self):
        states = State.objects.paginate(page=page_num(), per_page=per_page())
        total_states = State.objects.count()
        data = []
        if states:
            for state in states.items:
                data.append({
                    'id': str(state['id']),
                    'title': state['title'][get_locale()][0],
                    'code': state['code']
                })
            return make_response(jsonify(
                data=data,
                language=get_locale(),
                links=pagination_links(states, total_states),
                meta=pagination_meta_data(states, total_states)
            ))

        return make_response(jsonify({'message': 'No records found'})), 404


# Define the API resource
state_view = StateView.as_view('state_view')


# Add the url rule for registering a user
meta_data_blueprint.add_url_rule(
    '/states',
    view_func=state_view,
    methods=['GET'])
