from app import create_app
from flast_testing import TestCase


app = create_app()


class BaseTest(TestCase):

    def create_app(self):
        app.config.from_object('instance.config.TestingConfig')
        return app
