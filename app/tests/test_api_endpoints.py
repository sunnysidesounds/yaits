from flask import Flask
import unittest
from app import db
from app import api
from config import UnitTestConfig
from flask import jsonify


class BasicEndpointsTests(unittest.TestCase):

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
        print(data)
        self.assertEqual(response.status_code, 200)

    def test_api_project_by_id_response(self):
        response = self.app.get('/api/project?id=3', follow_redirects=True)
        data = response.get_json()
        print(data)
        self.assertEqual(response.status_code, 200)

    def test_api_new_project_response(self):
        pass

    # ISSUES TESTS

    def test_api_issues_response(self):
        response = self.app.get('/api/issues', follow_redirects=True)
        data = response.get_json()
        print(data)
        self.assertEqual(response.status_code, 200)

    # USERS TESTS


if __name__ == "__main__":
    unittest.main()