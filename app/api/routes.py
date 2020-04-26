from flask import Blueprint
from flask_restful import Api

from .resources import IssuesResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# get a list of issues
api.add_resource(IssuesResource, '/issues', methods=['GET'], endpoint='issues')
# search issues via attribute criteria matching
api.add_resource(IssuesResource, '/issues/search', methods=['GET'], endpoint='issue_search')
# get a issue by unique id
api.add_resource(IssuesResource, '/issue', methods=['GET'], endpoint='issue')
# create a new issue
api.add_resource(IssuesResource, '/issue/new', methods=['POST'], endpoint='issue_new')
# update an issue
api.add_resource(IssuesResource, '/issue/update', methods=['POST'], endpoint='issue_update')
# delete an issue
api.add_resource(IssuesResource, '/issue/delete', methods=['DELETE'], endpoint='issue_delete')