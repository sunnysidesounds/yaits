from flask import Flask
import json
import unittest
from app import db
from app import api
from config import UnitTestConfig


class BasicEndpointsTests(unittest.TestCase):

    """
    Basic endpoint tests
    - test for 200 response
    - test for valid JSON
    """

    def setUp(self):
        app = Flask(__name__)
        app = UnitTestConfig(app).set_config()
        db.init_app(app)
        api.init_app(app)
        self.app = app.test_client()

    def tearDown(self):
        pass

    # PROJECTS TESTS

    def test_api_projects_response(self):
        response = self.app.get('/api/projects', follow_redirects=True)
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.is_valid_json(data), True)

    def test_api_project_by_id_response(self):
        response = self.app.get('/api/project?id=3', follow_redirects=True)
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.is_valid_json(data), True)

    def test_api_new_project_response(self):
        payload = json.dumps({
            "name": "TEST",
            "description": "This is a test description"
        })
        response = self.app.post('/api/project', headers={"Content-Type": "application/json"}, data=payload)
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.is_valid_json(data), True)

    # ISSUES TESTS

    def test_api_issues_response(self):
        response = self.app.get('/api/issues', follow_redirects=True)
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.is_valid_json(data), True)

    def test_api_search_issues_response(self):
        response = self.app.get('/api/issues?like_name=D', follow_redirects=True)
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.is_valid_json(data), True)

    def test_api_search_issues_multi_response(self):
        response = self.app.get('/api/search/issues?like_name=D&priority_level=1&status=OPEN', follow_redirects=True)
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.is_valid_json(data), True)

    def test_api_issue_by_id_response(self):
        response = self.app.get('/api/issue?id=3', follow_redirects=True)
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.is_valid_json(data), True)

    def test_api_new_issue_response(self):
        payload = json.dumps({
            "project_id": 1,
            "name": "Test Issue",
            "description": "Test Description",
            "priority_level": 1,
            "assigned_to_user_id": 1,
            "created_by_user_id": 1,
            "status": "OPEN"

        })
        response = self.app.post('/api/issue', headers={"Content-Type": "application/json"}, data=payload)
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.is_valid_json(data), True)

    # USERS TESTS
    def test_api_users_response(self):
        response = self.app.get('/api/users', follow_redirects=True)
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.is_valid_json(data), True)

    def test_api_new_user_response(self):
        payload = json.dumps({
            "username": "TesterInsert",
            "first_name": "FirstTest",
            "last_Name": "LastEmail",
            "email": "test@test.com"
        })
        response = self.app.post('/api/user', headers={"Content-Type": "application/json"}, data=payload)
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.is_valid_json(data), True)

    def is_valid_json(self, data):
        try:
            json.dumps(data)
            return True
        except ValueError:
            return False



if __name__ == "__main__":
    unittest.main()