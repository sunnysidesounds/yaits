# Yaits Service
 Issue tracking service for Unity Technologies

## OVERVIEW

### Technical Details:
- Flask Python Web Service: https://flask.palletsprojects.com/en/1.1.x/
- MYSQL 8.0.19
- Python 3.8
- Docker 2.2.0.5


## SETUP
To setup this service, please follow these steps.

1. Download and install Docker Desktop: https://www.docker.com/products/docker-desktop
2. Pull down from git or unzip the service source code.
3. Get to the root directory of the service `cd /path-to-project/yaits/`
4. Build the service: `docker-compose build --no-cache`
5. Launch the service and db containers: `docker-compose up`
6. Once up and running visit any of the endpoint urls in the ***ENDPOINTS*** section.


## AVAILABLE ENDPOINTS:
These are the current available endpoints for this service:

##### PROJECT ENDPOINTS

- ***GET all projects***
    - `curl -X GET 'http://localhost:5000/api/projects`

- ***GET project by ID***
    - `curl -X GET 'http://localhost:5000/api/project?id=3`

- ***POST new Project***
```
curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"name":"This is a test project issue", "description":"This is a description"}' \
    http://localhost:5000/api/project`
```

- ***DELETE new Project**
    - TODO

##### ISSUE ENDPOINTS

- ***GET all Issues***
    - `curl -X GET 'http://localhost:5000/api/issues`

- ***SEARCH for Issues***
    - `curl -X GET 'http://localhost:5000/api/search/issues?like_name=D'`
    - `curl -X GET 'http://localhost:5000/api/search/issues?like_name=D&priority_level=1'`
    - `curl -X GET 'http://localhost:5000/api/search/issues?like_name=D&priority_level=1&status=OPEN'`


- ***GET Issue by ID***
    - `curl -X GET 'http://localhost:5000/api/issue?id=3'`

- ***POST new issue***
```
curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"project_id":1,"name":"This is a test insert issue", "description":"This is a description", "priority_level": 2, "assigned_to_user_id": 1, "created_by_user_id": 1, "status": "OPEN"}' \
    http://localhost:5000/api/issue
```

- ***DELETE issue by ID***
    - `curl -X DELETE http://localhost:5000/api/issue?id=9`

##### USER ENDPOINTS

- ***GET all users***
    - `curl -X GET 'http://localhost:5000/api/users'`

- ***GET user by ID***
    - `curl -X GET 'http://localhost:5000/api/user?id=1'`

- ***POST a new user***
```
curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"username":"tester", "first_name":"Jason", "last_name":"Alexander", "email": "jasonralexander@gmail.com"}' \
    http://localhost:5000/api/user
```






