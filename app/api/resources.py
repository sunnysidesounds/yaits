from flask import request
from flask_restful import Resource, reqparse
from app.utils import response_json
from app import constants
from .models import ProjectModel, IssueModel, UserModel
from .query_definitions import ISSUES_QUERY_ALL, ISSUES_QUERY_ONE, PROJECT_QUERY, USER_QUERY
from app.db import db


parser = reqparse.RequestParser()
parser.add_argument('id', type=int)
parser.add_argument('like_name', type=str)
parser.add_argument('issue_name', type=str)
parser.add_argument('project_name', type=str)
parser.add_argument('priority_level', type=int)
parser.add_argument('status', type=str)


class Users(Resource):
    def get(self):
        return QueryToResponseJSON(USER_QUERY).get_all()


class User(Resource):
    def get(self):
        args = parser.parse_args()
        user_id = args['id']
        data = None
        if user_id:
            query = PROJECT_QUERY + "WHERE id = {userId}".format(userId=user_id)
            return QueryToResponseJSON(query).get_one()
        else:
            return response_json(True, data, constants.NO_USER_ID)

    def post(self):
        args = parser.parse_args()
        user_id = args['id']
        data = request.get_json(force=True)
        if user_id:
            query = PROJECT_QUERY + "WHERE id = {userId}".format(userId=user_id)
            user_json = QueryToResponseJSON(query).get_one()['response']
            user_model = UserModel()
            user_model.update(user_id, {"username": data['username'] if 'username' in data else user_json['username'],
                                        "first_name": data['first_name'] if 'first_name' in data else user_json['first_name'],
                                        "last_name": data['last_name'] if 'last_name' in data else user_json['last_name'],
                                        "email": data['email'] if 'email' in data else user_json['email']})

            return response_json(True, data, None)
        else:
            if "username" not in data:
                return response_json(True, data, constants.NO_USERNAME)
            if "first_name" not in data:
                return response_json(True, data, constants.NO_FIRST_NAME)
            if "last_name" not in data:
                return response_json(True, data, constants.NO_LAST_NAME)
            if "email" not in data:
                return response_json(True, data, constants.NO_EMAIL)

            if not self.is_username_exist(data['username']):
                user_model = UserModel(
                    username=data['username'],
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    email=data['email'],
                )
                user_model.save()
                return response_json(True, data, None)
            else:
                return response_json(True, data, constants.NO_USERNAME)

    def is_username_exist(self, username):
        query = USER_QUERY + "WHERE username = '{username}'".format(username=username)
        return QueryToResponseJSON(query).exists()


class Projects(Resource):
    def get(self):
        return QueryToResponseJSON(PROJECT_QUERY).get_all()


class Project(Resource):
    def get(self):
        args = parser.parse_args()
        project_id = args['id']
        data = None
        if project_id:
            query = PROJECT_QUERY + "WHERE id = {projectId}".format(projectId=project_id)
            return QueryToResponseJSON(query).get_one()
        else:
            return response_json(True, data, constants.NO_ISSUE_ID)

    def post(self):
        args = parser.parse_args()
        project_id = args['id']
        data = request.get_json(force=True)
        # Update record
        if project_id:
            query = PROJECT_QUERY + "WHERE id = {projectId}".format(projectId=project_id)
            project_json = QueryToResponseJSON(query).get_one()['response']
            project_model = ProjectModel()
            project_model.update(project_id, {"name": data['name'] if 'name' in data else project_json['name'],
                                              "description": data['description'] if 'description' in data else project_json['description']})
        # New record
        else:
            if "name" not in data:
                return response_json(True, data, constants.NO_PROJECT_NAME)
            if "description" not in data:
                data['description'] = constants.DEFAULT_DESCRIPTION

            project_model = ProjectModel(
                name=data['name'],
                description=data['description'],
            )
            project_model.save()

        return response_json(True, data, None)

    def is_project_exist(project_id):
        query = PROJECT_QUERY + "WHERE id = {projectId}".format(projectId=project_id)
        return QueryToResponseJSON(query).exists()


class Issues(Resource):
    def get(self):
        return QueryToResponseJSON(ISSUES_QUERY_ALL).get_all()


class Issue(Resource):
    def get(self):
        args = parser.parse_args()
        issue_id = args['id']
        data = None

        if issue_id:
            query = ISSUES_QUERY_ONE + "WHERE i.id = {issueId}".format(issueId=issue_id)
            return QueryToResponseJSON(query).get_one()
        else:
            return response_json(True, data, constants.NO_ISSUE_ID)

    def post(self):
        args = parser.parse_args()
        issue_id = args['id']
        data = request.get_json(force=True)
        # Update record
        if issue_id:
            query = ISSUES_QUERY_ONE + "WHERE i.id = {issueId}".format(issueId=issue_id)
            issue_json = QueryToResponseJSON(query).get_one()['response']
            issue_model = IssueModel()
            issue_model.update(issue_id, {"project_id": data['project_id'] if 'project_id' in data else issue_json['project_id'],
                                         "name": data['name'] if 'name' in data else issue_json['name'],
                                         "description": data['description'] if 'description' in data else issue_json['description'],
                                          "priority_level": data['priority_level'] if 'priority_level' in data else issue_json['priority_level'],
                                          "assigned_to_user_id": data['assigned_to_user_id'] if 'assigned_to_user_id' in data else issue_json['assigned_to_user_id'],
                                          "created_by_user_id": data['created_by_user_id'] if 'created_by_user_id' in data else issue_json['created_by_user_id'],
                                          "status": data['status'] if 'status' in data else issue_json['status']})
       # New record
        else:
            if "project_id" not in data:
                return response_json(True, data, constants.NO_PROJECT_ID)

            if "name" not in data:
                return response_json(True, data, constants.NO_ISSUE_NAME)

            if "created_by_user_id" not in data:
                return response_json(True, data, constants.NO_CREATED_BY_USER_ID)

            if "assigned_to_user_id" not in data:
                data['assigned_to_user_id'] = data['created_by_user_id']

            # Set default is not provided
            if "description" not in data:
                data['description'] = constants.DEFAULT_DESCRIPTION

            if "priority_level" not in data:
                data['priority_level'] = 1

            if "status" not in data:
                data['status'] = "OPEN"

            if Project.is_project_exist(data['project_id']):

                issue_model = IssueModel(
                    project_id=data['project_id'],
                    name=data['name'],
                    description=data['description'],
                    priority_level=data['priority_level'],
                    assigned_to_user_id=data['assigned_to_user_id'],
                    created_by_user_id=data['created_by_user_id'],
                    status=data['status'],
                )
                issue_model.save()

        return response_json(True, data, None)

    def delete(self):
        args = parser.parse_args()
        issue_id = args['id']
        if self.is_issue_exist(issue_id):
            IssueModel.query.filter_by(id=issue_id).delete()
            db.session.commit()
            return response_json(True, {"issue_id": issue_id}, constants.ISSUE_DELETED)
        else:
            return response_json(True, {"issue_id": issue_id}, constants.NO_ISSUE_ID)

    def is_issue_exist(self, issue_id):
        query = ISSUES_QUERY_ONE + "WHERE i.id = {issueId}".format(issueId=issue_id)
        return QueryToResponseJSON(query).exists()


class SearchIssues(Resource):

    def get(self):
        args = parser.parse_args()
        search_parameters = []
        query = ISSUES_QUERY_ALL
        for key, val in args.items():
            if val is not None:
                search_parameters.append({"key": key, "val": val})

        for i in range(len(search_parameters)):
            if i == 0:
                if 'like_name' in search_parameters[i]['key']:
                    query += "WHERE i.name LIKE '{likeName}%'".format(likeName=search_parameters[i]['val'])
                else:
                    query +="WHERE i.{columnName} = '{valueName}'".format(columnName=search_parameters[i]['key'],
                                                                      valueName=search_parameters[i]['val'])
            else:
                if 'like_name' in search_parameters[i]['key']:
                    query += "AND i.name LIKE '{likeName}%' ".format(likeName=search_parameters[i]['val'])
                else:
                    query +="AND i.{columnName} = '{valueName}' ".format(columnName=search_parameters[i]['key'],
                                                                    valueName=search_parameters[i]['val'])

        return QueryToResponseJSON(query).get_all()


class QueryToResponseJSON:

    def __init__(self, query):
        self.query = query

    def get_one(self):
        data = dict(db.engine.execute(self.query).fetchone())
        if data:
            return response_json(True, data, None)
        else:
            return response_json(True, data, constants.NO_DATA)

    def get_all(self):
        data = db.engine.execute(self.query).fetchall()
        data = [dict(r) for r in data]
        if data:
            return response_json(True, data, None)
        else:
            return response_json(True, data, constants.NO_DATA)

    def exists(self):
        data = db.engine.execute(self.query).fetchone()
        return True if data else False
