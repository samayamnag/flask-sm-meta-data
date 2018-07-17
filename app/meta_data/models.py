from app import db


class State(db.Document):
    state_id = db.IntField(unique=True)
    title = db.DictField()
    code = db.StringField(max_lenght=255)

    meta = {
        'collection': 'states',
        'indexes': [
            {
                'fields': ['state_id'],
                'unique': True,
                'name': 'states_state_id_unique',
            },
            {
                'fields': ['title.*'],
                'name': 'states_title_index',
            }
        ]
        }


class District(db.Document):
    district_id = db.IntField()
    state_id = db.ObjectIdField()
    title = db.DictField()
    code = db.StringField(max_lenght=255)

    meta = {
        'collection': 'districts',
        'indexes': [
            {
                'fields': ['district_id'],
                'unique': True,
                'name': 'districts_district_id_unique',
            },
            {
                'fields': ['state_id'],
                'name': 'districts_state_id_index',
            },
            {
                'fields': ['title.*'],
                'name': 'districts_title_index',
            }
        ]
        }


class City(db.Document):
    city_id = db.IntField()
    district_id = db.ObjectIdField()
    state_id = db.ObjectIdField()
    title = db.DictField()
    code = db.StringField(max_lenght=255)    
    ward_count = db.IntField(default=0)
    population_bucket = db.IntField()
    population = db.IntField()
    census_code = db.IntField()
    coordinates = db.PointField()

    meta = {
        'collection': 'cities',
        'indexes': [
            {
                'fields': ['city_id'],
                'unique': True,
                'name': 'cities_city_id_unique',
            },
            {
                'fields': ['state_id'],
                'name': 'cities_state_id_index',
            },
            {
                'fields': ['district_id'],
                'name': 'cities_district_id_index',
            },
            {
                'fields': ['title.*'],
                'name': 'cities_title_index',
            }
        ]
        }


class CivicAgency(db.Document):
    civic_agency_id = db.IntField()
    city_id = db.IntField()
    district_id = db.ObjectIdField()
    state_id = db.ObjectIdField()
    title = db.DictField()

    meta = {
        'collection': 'civic_agencies',
        'indexes': [
            {
                'fields': ['civic_agency_id'],
                'unique': True,
                'name': 'civic_agencies_civic_agency_id_id_unique',
            },
            {
                'fields': ['district_id'],
                'name': 'civic_agencies_district_id_index',
            },
            {
                'fields': ['state_id'],
                'name': 'civic_agencies_state_id_index',
            },
            {
                'fields': ['city_id'],
                'name': 'civic_agencies_city_id_index',
            },
            {
                'fields': ['title.*'],
                'name': 'civic_agencies_title_index',
            }
        ]
        }


'''
from mongoengine import *
connect('dj_sm_meta_data')
State.objects(title__hi__in=["hima hindi"]).count()
'''
