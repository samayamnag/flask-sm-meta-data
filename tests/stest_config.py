import unittest
from app import create_app
from decouple import config
from base import BaseTestCase
from flask import current_app
from flask_testing import TestCase


app = create_app()


class TestDevelopmentConfig(TestCase):

    def create_app(self):
        app.config.from_object('instance.config.Config')
        return app

    def test_app_is_development(self):
        self.assertFalse(current_app.config['TESTING'])
        self.assertFalse(current_app is None)


class TestTestingConfig(TestCase):

    def create_app(self):
        app.config.from_object('instance.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])


class TestProductionConfig(TestCase):

    def create_app(self):
        app.config.from_object('instance.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertFalse(current_app.config['TESTING'])


if __name__ == '__main__':
    unittest.main()
