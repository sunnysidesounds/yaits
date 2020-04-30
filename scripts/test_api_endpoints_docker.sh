



curl -X GET 'http://localhost:5000/api/projects'

curl -X GET 'http://localhost:5000/api/project?id=3'

curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"name":"This is a test project issue", "description":"This is a description"}' \
    http://localhost:5000/api/project

curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"name":"This is a test project issue", "description":"This is a description"}' \
    http://localhost:5000/api/project

curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"description":"This is a description"}' \
    http://localhost:5000/api/project?id=1

curl -X GET 'http://localhost:5000/api/issues'

curl -X GET 'http://localhost:5000/api/search/issues?like_name=D&priority_level=1&status=OPEN'

curl -X GET 'http://localhost:5000/api/issue?id=3'

curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"project_id":1,"name":"This is a test insert issue", "description":"This is a description", "priority_level": 2, "assigned_to_user_id": 1, "created_by_user_id": 1, "status": "OPEN"}' \
    http://localhost:5000/api/issue

curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"project_id":1,"name":"This is a test insert issue", "priority_level": 2, "assigned_to_user_id": 1, "created_by_user_id": 1, "status": "OPEN"}' \
    http://localhost:5000/api/issue?id=3

curl -X GET 'http://localhost:5000/api/users'

curl -X GET 'http://localhost:5000/api/user?id=1'

curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"username":"tester", "first_name":"Jason", "last_name":"Alexander", "email": "jasonralexander@gmail.com"}' \
    http://localhost:5000/api/user