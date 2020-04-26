from app.db import marshmallow
from marshmallow_enum import EnumField
from .models import StatusType, Issue


class IssuesSchema(marshmallow.Schema):
    status = EnumField(StatusType, by_value=True)
    """
    This class represents the wallet schema.
    """
    class Meta:
        model = Issue
        fields = (
            'id', 'project_id', 'name', 'description',
            'priority_level', 'assigned_to_user_id', 'created_by_user_id',
            'status', 'last_updated'
        )

issue_schema = IssuesSchema()
issues_schema = IssuesSchema(many=True)