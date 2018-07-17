from decouple import config


class Config(object):

    ENV = config('APP_ENV', default='production')
    DEBUG = config('APP_DEBUG', default=True, cast=bool)
    TESTING = False
    LANGUAGES = {
        'en': 'English', 
        'hi': 'Hindi', 
        'te': 'Telugu',
        'ta': 'Tamil',
        'kn': 'Kannada',
        'ml': 'Malayalam',
        'bn': 'Beganli',
        'mr': 'Marathi',
        },
    BABEL_DEFAULT_LOCALE = config('APP_LOCALE', default='en')
    MONGODB_SETTINGS = [
        {
            'db': config('MONGO_DB_DATABASE', default='sm_meta_data'),
            'host': config('MONGO_DB_HOST', default='sm_meta_data'),
            'port': config('MONGO_DB_PORT', 27017, cast=int),
            'alias': 'default',
            'connect': False,
        },
        {
            'db': config('MONGO_DB_DATABASE', default='sm_meta_data'),
            'host': config('MONGO_DB_HOST', default='sm_meta_data'),
            'port': config('MONGO_DB_PORT', 27017, cast=int),
            'alias': 'testing',
            'connect': False,
        }
    ]


class TestingConfig(Config):
    TESTING = True
    MONGODB_SETTINGS = [
        {
            'db': config('MONGO_DB_TESTING_DATABASE', default='testing_sm_meta_data'),
            'host': config('MONGO_DB_TESTING_HOST', default='localhost'),
            'port': config('MONGO_DB_TESTING_PORT', 27017, cast=int),
            'alias': 'default',
            'connect': True,
        },
    ]

class ProductionConfig(Config):
    DEBUG = False
