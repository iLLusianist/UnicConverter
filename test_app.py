import unittest
from flask_testing import TestCase
from app import app
from parameterized import parameterized

class AppTest(TestCase):

    @staticmethod
    def create_app():
        app.config['TESTING'] = True
        return app

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    @parameterized.expand([
        (123, 'celsius', 'fahrenheit', 'temperature', '253.4 °F'),
        (32, 'fahrenheit', 'celsius', 'temperature', '0.0 °C'),
        (-40, 'celsius', 'kelvin', 'temperature', '233.15 K'),
        (-856, 'fahrenheit', 'celsius', 'temperature', '-493.33 °C'),
    ])
    def test_convert(self, value, converted_from, converted_to, unit, expected_result):
        with app.test_client() as client:
            response = client.post(
                '/convert',
                json = {
                    'value': value,
                    'converted_from': converted_from,
                    'converted_to': converted_to,
                    'unit': unit
                }
            )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_result)

if __name__ == '__main__':
    unittest.main()