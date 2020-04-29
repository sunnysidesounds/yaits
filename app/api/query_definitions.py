USER_QUERY = """SELECT id, username, first_name, last_name, email FROM users """

PROJECT_QUERY = """SELECT id, name, description FROM projects """

ISSUES_QUERY_ALL = """SELECT 
    i.id as issue_id, 
    p.name as project_name, 
    i.name as issue_name, 
    i.description, 
    i.priority_level, 
    u.username as created_by_username, 
    i.status
    FROM issues i
    JOIN projects p on p.id = i.project_id 
    JOIN users u on u.id = i.created_by_user_id """

ISSUES_QUERY_ONE = """SELECT 
    i.id as issue_id, 
    p.name as project_name, 
    i.name as issue_name, 
    i.description, 
    i.priority_level, 
    uu.username as assigned_to_username, 
    u.username as created_by_username, 
    i.status
    FROM issues i
    JOIN projects p on p.id = i.project_id 
    JOIN users u on u.id = i.created_by_user_id 
    JOIN users uu on uu.id = i.assigned_to_user_id """