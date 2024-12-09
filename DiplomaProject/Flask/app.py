from flask import Flask, jsonify, request, render_template
from flask_restful import Api, Resource
from models import db, Task, task_schema, tasks_schema
from crud import create_task, delete_task, get_tasks

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

api = Api(app)

class TaskListResource(Resource):
    def get(self):
        tasks = get_tasks()
        return tasks_schema.dump(tasks), 200

    def post(self):
        title = request.json['title']
        description = request.json.get('description', '')
        due_date = request.json['due_date']
        task = create_task(title, description, due_date)
        return task_schema.dump(task), 201

class TaskResource(Resource):
    def delete(self, task_id):
        task = delete_task(task_id)
        if task:
            return {"detail": "Task deleted"}, 200
        return {"detail": "Task not found"}, 404

api.add_resource(TaskListResource, '/tasks')
api.add_resource(TaskResource, '/tasks/<int:task_id>')

@app.route('/', methods=['GET'])
def index():
    tasks = get_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/tasks/new', methods=['GET', 'POST'])
def task_form():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form.get('description', '')
        due_date = request.form['due_date']
        create_task(title, description, due_date)
        return jsonify({"message": "Task created"}), 201
    return render_template('task_form.html')

if __name__ == '__main__':
    app.run(debug=True)
