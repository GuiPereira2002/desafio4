import unittest
from app import app
import json

class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_calculator_4_success(self):
        response = self.app.post('/calculator_4', 
                                 data=json.dumps([1, 2, 3, 4, 5]), 
                                 content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['average'], 3)

    def test_calculator_4_invalid_input(self):
        response = self.app.post('/calculator_4', 
                                 data=json.dumps("invalid input"), 
                                 content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], "Invalid input, please provide a list of numbers.")

    def test_calculator_4_empty_list(self):
        response = self.app.post('/calculator_4', 
                                 data=json.dumps([]), 
                                 content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['average'], 0)

if __name__ == '__main__':
    unittest.main()
