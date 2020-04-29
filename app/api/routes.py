from flask import Blueprint
from flask_restful import Api

from .resources import Issues, Issue, Projects, Project, Users, User, SearchIssues

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# ISSUES

# get a list of issues
api.add_resource(Issues, '/issues', methods=['GET'], endpoint='issues')
# search issues via attribute criteria matching
api.add_resource(SearchIssues, '/search/issues', methods=['GET'], endpoint='search_issues')
# get a issue by unique id
api.add_resource(Issue, '/issue', methods=['GET'], endpoint='issue_by_id')
# create a new or update issue
api.add_resource(Issue, '/issue', methods=['POST'], endpoint='issue_new')
# delete an issue
api.add_resource(Issue, '/issue', methods=['DELETE'], endpoint='issue_delete')

# PROJECTS

# get a list of projects
api.add_resource(Projects, '/projects', methods=['GET'], endpoint='projects')
# get project by id:
api.add_resource(Project, '/project', methods=['GET'], endpoint='project_by_id')
# create a new project
api.add_resource(Project, '/project', methods=['POST'], endpoint='project_new')

# USERS

# Get all users
api.add_resource(Users, '/users', methods=['GET'], endpoint='users')
# Get user by id:
api.add_resource(User, '/user', methods=['GET'], endpoint='user')
# Create new user
api.add_resource(User, '/user', methods=['POST'], endpoint='user_new')

