import unittest
from base import BaseTestCase
from flask_testing import TestCase
from app.meta_data.models import State
from instance.config import TestingConfig
from app import create_app
from decouple import config


app = create_app(TestingConfig)

class TestStateModel(TestCase):

    def create_app(self):
        return app

    def test_insert_state(self):
        state = State(
            state_id=1,
            title={'en': ['Bant'], 'hi': ['Hindi ban']},
            code='bant').save(using='testing')



        self.assertEqual(200, 200)


if __name__ == '__main__':
    unittest.main()