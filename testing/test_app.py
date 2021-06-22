from flask import url_for
from flask_testing import TestCase
from app import app
import os

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',    
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(os.getenv('mytext'), response.data)

