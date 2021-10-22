from unittest import TestCase
from simple_app import create_app


class BaseSimpleAppTestClass(TestCase):
    def setUp(self):
        self.app = create_app({
            'TESTING': True,
            'WTF_CSRF_ENABLED': False
        })
        self.client = self.app.test_client()
        self.runner = self.app.test_cli_runner()

    def test_index(self):
        response = self.client.get("/")
        self.assertIn(b'Ackermann Inputs', response.data)
        self.assertEqual(response.status_code, 200)
