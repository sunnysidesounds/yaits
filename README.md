# Yaits Service
 Issue tracking service for Unity Technologies

## OVERVIEW

### Design Description
This is a basic, but easily extendable issue tracking service with projects, issues and users. Users can creates projects
with issues and assign these issues to each other.

### Trade-offs/Compromises, Scale, or Performance Issue Considerations
- For high-performance web service using Flask framework might not be the best web framework to service millions of user, like
JIRA. Languages like Java and Frameworks like Spring, Play or any J2EE application/service framework would probably pretty be suited
for specific applications like this. But there has been sites like Obama's 2012 election site and Twilio are both built on this framework and
have handle requests at large scale.
- Using any cloud service, such as AWS or GCP using a load balancer and containerized app clusters should be able to scale and handle each part
of the application.

### Ideas To Improve/Extend Service
1. TODO: Move queries to ***SQLAlchemy*** ORM
    - Right now some of the queries aren't fully utilizing the ***SQLAlchemy*** ORM models due to the table joins
2. TODO: Validate and make sure the query strings being built are parameterized properly.
    - If we switched to using the full ***SQLAlchemy*** ORM for queries this would completely go away.
3. TODO: Add unit tests
    - We have integration / endpoint tests, we should write unit tests to test utility functions..etc
4. TODO: Add an in-memory database for integration / endpoint tests.
    - Right now we are test CRUD functionality on a MySQL database.
5. TODO: Add in authentication.
    - As there are user endpoints to create users. There no validation, authentication. This should be added.

### Technical Details
- Flask Python Web Service: https://flask.palletsprojects.com/en/1.1.x/
- MYSQL 8.0.19
- Python 3.8

### Database Schemas

***Projects Schema***
- Additional columns that should be added: __created_by_user_id__
```
CREATE TABLE IF NOT EXISTS projects (
    `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NULL,
    `description` varchar(500) NULL,
    `last_updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;

```

***Issues Schema***
- Foreign key constraint ids between project (project_id) and user (created_by_user_id) tables.
```
CREATE TABLE IF NOT EXISTS issues (
   `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
   `project_id` int(10) UNSIGNED NOT NULL,
   `name` varchar(255) NULL,
   `description` varchar(500) NULL,
   `priority_level` int(10) UNSIGNED NOT NULL DEFAULT '1',
   `assigned_to_user_id` int(10) UNSIGNED NOT NULL DEFAULT 0,
   `created_by_user_id` int(10) UNSIGNED NOT NULL,
   `status` ENUM('OPEN', 'INPROGRESS', 'REOPENED', 'RESOLVED', 'CLOSED') NOT NULL,
   `last_updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
   PRIMARY KEY (id),
   KEY `project_id` (`project_id`),
   KEY `index_name` (`name`(255)),
   CONSTRAINT `project_id_constraint_1` FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`),
   CONSTRAINT `created_by_user_id_constraint_1` FOREIGN KEY (`created_by_user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;
```

***Users Schema***
```
CREATE TABLE IF NOT EXISTS users (
     `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
     `username` varchar(125) NULL,
     `first_name` varchar(125) NULL,
     `last_name` varchar(125) NULL,
     `email` varchar(255) NULL,
     `last_updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
     PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;
```

## Setup
To setup this service, please follow these steps.

##### Setup with Docker

***Prerequisites***
- Docker 2.2.0.5

1. Download and install Docker Desktop: https://www.docker.com/products/docker-desktop
2. Pull down from git or unzip the yaits/ service source code.
3. Get to the root directory of the service `cd /path-to-project/yaits/`
4. Build the service: `docker-compose build --no-cache`
5. Launch the service and db containers: `docker-compose up`
6. Once up and running visit any of the endpoint urls in the ***ENDPOINTS*** section.

##### Setup Locally

***Prerequisites***
- MYSQL 8.0.19
- Python 3.8
- pip / easy_install

1. Install virtualenv using `pip install virtualenv`
2. Pull down from git or unzip the yaits/ service source code.
3. Get to the root directory of the service `cd /path-to-project/yaits/`
4. Create a new virtual environment `virtualenv venv`
5. Active the new virtual environment `source venv/bin/activate`
6. Install requirements into virtual environment `venv/bin/pip install -r requirements.txt`
    - This will install Flask framework, mysql connector...etc.
7. Login to `mysql -u USER -pPASS` and create a new database `CREATE DATABASE testdb;`
8. Import the test data `mysql -u USER -pPASS testdb < ./sql/yaits_sample_db.sql`
9. Start the application by `venv/bin/python app.py`
10. Once up and running visit any of the endpoint urls in the ***ENDPOINTS*** section.


## Available Endpoints:
These are the current available endpoints for this service.

##### PROJECT ENDPOINTS

- ***GET all projects***
    - `curl -X GET 'http://localhost:5000/api/projects'`

- ***GET project by ID***
    - `curl -X GET 'http://localhost:5000/api/project?id=3'`

- ***POST new Project***
```
curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"name":"This is a test project issue", "description":"This is a description"}' \
    http://localhost:5000/api/project
```

- ***UPDATE a Project***
```
curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"description":"This is a description"}' \
    http://localhost:5000/api/project?id=1
```

##### ISSUE ENDPOINTS

- ***GET all Issues***
    - `curl -X GET 'http://localhost:5000/api/issues'`

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

- ***UPDATE a issue***
```
curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"project_id":1,"name":"This is a test insert issue", "priority_level": 2, "assigned_to_user_id": 1, "created_by_user_id": 1, "status": "OPEN"}' \
    http://localhost:5000/api/issue?id=3
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

- ***UPDATE a user***
```
curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"username":"tester", "first_name":"Jason", "last_name":"Alexander", "email": "jasonralexander@gmail.com"}' \
    http://localhost:5000/api/user?id=1
```

## Testing / Tests:

### Integration / Endpoint Tests:

##### Testing locally:
1. Currently to run tests you need to have setup the environment locally (See SETUP, locally above)
2. Once setup you can run this command to test all current endpoints:
    -  `venv/bin/python ./app/tests/test_api_endpoints.py`

##### Testing using Docker:
1. You can current run this bash script locally and it will hit all of the endpoints.
    - ` bash ./scripts/test_api_endpoints_docker.sh`







