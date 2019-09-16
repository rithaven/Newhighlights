import unittest
from flask import current_app
from app import create_app


class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the  classes in News
    '''

    def setUp(self):
        self.app = create_app('development')
        self.app_context = self.app.app_context()
        self.app_context.push()
    def tearDown(self):
        self.app_context.pop()

    def test_instance(self):
        self.assertFalse(current_app is None)