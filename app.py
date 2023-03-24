from flask import Flask, render_template, jsonify, abort, request

app = Flask(__name__)

uri = '/api/tasks'
persona = {'name': 'Ana Sofi', 'matricula': '185767'}

tasks = [
    {
        'id': 1,
        'name': 'cocinar algo bien sabroso',
        'status': True
    },
    {
        'id': 2,
        'name': 'limpiar la casa',
        'status': False
    },
]


@app.route("/")
def hello_world():
    return render_template('index.html', data=persona)


@app.route("/saluda")
def saluda():
    return "Que onda"

# API


@app.route(uri, methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route(uri+'/<int:id>', methods=['GET'])
def get_task(id):
    this_task = 0
    for task in tasks:
        if task['id'] == id:
            this_task = task
    if this_task == 0:
        abort(404)
    return jsonify({'task': this_task})


@app.route(uri, methods=['POST'])
def create_task():
    if request.json:
        task = {
            'id': len(task)+1,
            'name': request.json('name'),
            'status': False
        }
        task.append(task)
        return jsonify({'tasks': tasks}), 201
    else:
        abort(404)


@app.route(uri+'/<int:id>', methods=['PUT'])
def update_task(id):
    if request.json:
        this_task = [task for task in tasks if task['id'] == id]
        if this_task:
            if request.json:
                if request.json.get['name']:
                    this_task[0]['name'] = request.jason['name']
                if request.json.get['status']:
                    this_task[0]['status'] = request.jason['status']
                return jsonify({'task': this_task[0]}), 201
        else:
            abort(404)
    else:
        abort(404)


@app.route(uri+'/<int:id>', methods=['DELETE'])
def delete_task(id):
    this_task = [task for task in tasks if task['id'] == id]
    if this_task:
        tasks.remove(this_task[0])
        return jsonify({'tasks': tasks})
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)
