from app import create_app
from flask_testing import TestCase
from instance.config import TestingConfig


class BaseTestCase(TestCase):

    def create_app(self):
        app = create_app(TestingConfig)
        return app
