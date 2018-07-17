from app.meta_data.models import State, District, City, CivicAgency
from app.utils import (
    get_locale, per_page, page_num,
    pagination_meta_data, pagination_links
)
from flask import request
from flask_mongoengine.MongoEngine.queryset.visitor import Q



def get_states():
    states = State.objects.paginate(page=page_num(), per_page=per_page())
    total_states = State.objects.count()
    data = []
    response = {}
    if states:
        for state in states.items:
            data.append({
                'id': str(state['id']),
                'title': state['title'][get_locale()][0],
                'code': state['code']
            })
        response = {
            'data': data,
            'links': pagination_links(states, total_states),
            'meta': pagination_meta_data(states, total_states)
        }
    return response

def get_districts():
    state_id = request.args.get('state_id')
    if state_id:
        qs = District.objects(state_id=state_id)
        districts = qs.paginate(page=page_num(), per_page=per_page())
        total_districts = qs.count()
    else:
        districts = District.objects.paginate(page=page_num(), per_page=per_page())
        total_districts = District.objects.count()
    data = []
    response = {}
    if districts:
        for district in districts.items:
            data.append({
                'id': str(district['id']),
                'title': district['title'][get_locale()][0],
                'code': district['code']
            })
        response = {
            'data': data,
            'links': pagination_links(districts, total_districts),
            'meta': pagination_meta_data(districts, total_districts)
        }
    return response

def get_cities():
    cities = City.objects.paginate(page=page_num(), per_page=per_page())
    total_cities = City.objects.count()
    data = []
    response = {}
    if cities:  
        for city in cities.items:
            data.append({
                'id': str(city['id']),
                'title': city['title'][get_locale()][0],
                'code': city['code']
            })
        response = {
            'data': data,
            'links': pagination_links(cities, total_cities),
            'meta': pagination_meta_data(cities, total_cities)
        }
    return response

def get_civic_agencies():
    district_id = request.args.get('district_id')
    print(district_id)
    if district_id:
        qs = CivicAgency.objects(district_id=district_id)
        civic_agencies = qs.paginate(page=page_num(), per_page=per_page())
        total_civic_agencies = qs.count()
    else:
        civic_agencies = CivicAgency.objects.paginate(page=page_num(), per_page=per_page())
        total_civic_agencies = CivicAgency.objects.count()
    data = []
    response = {}
    if civic_agencies:
        for civic_agency in civic_agencies.items:
            data.append({
                'id': str(civic_agency['id']),
                'title': civic_agency['title'][get_locale()][0],
            })
        response = {
            'data': data,
            'links': pagination_links(civic_agencies, total_civic_agencies),
            'meta': pagination_meta_data(civic_agencies, total_civic_agencies)
        }
    return response