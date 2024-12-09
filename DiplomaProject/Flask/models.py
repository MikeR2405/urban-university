from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    due_date = db.Column(db.String(10))  # Дата в формате строка (или можно использовать db.Date)
    completed = db.Column(db.Boolean, default=False)

class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(allow_none=True)
    due_date = fields.Str(required=True)
    completed = fields.Bool()

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
