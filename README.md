# Yaits Service
 Issue tracking service for Unity Technologies


 ## SETUP


 ### RUNNING

 ### ENDPOINTS:

## Projects

#### Get all projects
curl -X GET 'http://localhost:5000/api/projects

### Get project by id
curl -X GET 'http://localhost:5000/api/project?id=3

### Post new Project
curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"name":"This is a test project issue", "description":"This is a description"}' \
    http://localhost:5000/api/project

## Issues

#### Get all Issues:
curl -X GET 'http://localhost:5000/api/issues

#### Search for Issues:

##### By like name
curl -X GET 'http://localhost:5000/api/search/issues?like_name=D'
curl -X GET 'http://localhost:5000/api/search/issues?like_name=D&priority_level=1'
curl -X GET 'http://localhost:5000/api/search/issues?like_name=D&priority_level=1&status=OPEN'

#### Get Issue by id:
curl -X GET 'http://localhost:5000/api/issue?id=3'

#### Post new issue:
curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"project_id":1,"name":"This is a test insert issue", "description":"This is a description", "priority_level": 2, "assigned_to_user_id": 1, "created_by_user_id": 1, "status": "OPEN"}' \
    http://localhost:5000/api/issue

#### Delete issue by id
curl -X DELETE http://localhost:5000/api/issue?id=9

## Users

#### Get all users
curl -X GET 'http://localhost:5000/api/users'

#### Get user by id
curl -X GET 'http://localhost:5000/api/user?id=1'

#### Post a new user:
curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"username":"tester", "first_name":"Jason", "last_name":"Alexander", "email": "jasonralexander@gmail.com"}' \
    http://localhost:5000/api/user






