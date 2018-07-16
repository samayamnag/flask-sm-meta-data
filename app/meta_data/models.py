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


'''
from mongoengine import *
connect('dj_sm_meta_data')
State.objects(title__hi__in=["hima hindi"]).count()
'''
