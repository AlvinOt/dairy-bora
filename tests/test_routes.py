import sys
import os

# Add the project directory to sys.path
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_dir)

import unittest
from app import app

class TestAddAnimalEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_add_animal_success(self):
        # Send a POST request with JSON data to simulate adding an animal
        response = self.app.post('/add_animal', json={
            'name': 'Nerea',
            'breed': 'Fresian',
            'birth_date': '2022-01-15',
            'gender': 'Female'
        })

        # Check if the response code is 201 (Created)
        self.assertEqual(response.status_code, 201)
        # Check if the response message matches the expected message
        self.assertEqual(response.get_json(), {"message": "Animal added successfully."})

    def test_add_animal_missing_data(self):
        # Send a POST request with missing data
        response = self.app.post('/add_animal', json={})

        # Check if the response code is 500 (Internal Server Error)
        self.assertEqual(response.status_code, 500)
        # Check if the response contains an error message
        self.assertIn("error", response.get_json())

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

