import unittest
from flask import url_for
from os import getenv
from unittest.mock import patch
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

# test for random name
class TestResponse(TestBase):
    def test_email_name(self):
        with patch('random.randint') as r:
            r.return_value = 1
            response = self.client.get(url_for('get_name'))
            self.assertIn(b'Friedrich', response.data)