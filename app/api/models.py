import enum
from app.db import db


class ProjectModel(db.Model):
    """
    This class represents the projects table.
    """
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=255))
    description = db.Column(db.String(length=500))
    last_updated = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return '<id: {}>'.format(self.id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, project_id, model):
        project = self.query.filter_by(id=project_id).first()
        project.name = model['name']
        project.description = model['description']
        db.session.commit()

class UserModel(db.Model):
    """
    This class represents the users table.
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=125))
    first_name = db.Column(db.String(length=125))
    last_name = db.Column(db.String(length=125))
    email = db.Column(db.String(length=255))
    last_updated = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return '<id: {}>'.format(self.id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, user_id, model):
        user = self.query.filter_by(id=user_id).first()
        user.username = model['username']
        user.first_name = model['first_name']
        user.last_name = model['last_name']
        user.email = model['email']
        db.session.commit()


class StatusType(enum.Enum):
    OPEN = "OPEN"
    INPROGRESS = "INPROGRESS"
    REOPENED = "REOPENED"
    RESOLVED = "RESOLVED"
    CLOSED = "CLOSED"


class IssueModel(db.Model):
    """
   This class represents the issues table.
   """
    __tablename__ = 'issues'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    name = db.Column(db.String(length=255))
    description = db.Column(db.String(length=500))
    priority_level = db.Column(db.Integer)
    assigned_to_user_id = db.Column(db.Integer)
    created_by_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    status = db.Column(db.Enum(StatusType))
    last_updated = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return '<id: {}>'.format(self.id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, issue_id, model):
        issue = self.query.filter_by(id=issue_id).first()
        issue.project_id = model['project_id']
        issue.name = model['name']
        issue.description = model['description']
        issue.priority_level = model['priority_level']
        issue.assigned_to_user_id = model['assigned_to_user_id']
        issue.created_by_user_id = model['created_by_user_id']
        issue.status = model['status']
        db.session.commit()