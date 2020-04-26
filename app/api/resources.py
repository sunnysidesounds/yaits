from flask_restful import Resource, reqparse
from app.utils import response_json, make_request
from app import constants
from .models import Project, Issue, User
from .schemas import issue_schema, issues_schema


parser = reqparse.RequestParser()
parser.add_argument('currency_code', type=str)
parser.add_argument('requested_amount', type=float)
parser.add_argument('no_of_operations', type=int)


class IssuesResource(Resource):

    def get(self):
        query = Issue.query.order_by('id')
        data = issues_schema.dump(query).data
        if data:
            return response_json(True, data, None)
        else:
            return response_json(True, data, constants.NO_DATA)

    def post(self):
        return "STUBBED POST"