from flask import render_template, request, redirect, url_for
from app import app, models, db

Task = models.Task

@app.route('/')
def index():
    title = 'My Personal Todo Application!'
    tasks = Task.query.all()
    return render_template("index.html", title=title, tasks=tasks)

# POST (Forms)
@app.route('/item/', methods=['POST'])
def add_item():
    # Get form data from
    taskName = request.form.get('itemName')
    taskDescription = request.form.get('itemDescription')
    new_item = Task(name=taskName, description=taskDescription)
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('index'))

# DELETE (Delete a specific task id)
@app.route('/task/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.filter_by(id=id).first()
    
    # Check if Task exists
    if (task != None):
        msg = {
            'message': 'Delete successful'
        }
        db.session.delete(item)
        db.session.commit()
        return jsonify(msg), 200
	
    # Task does not exist
    msg = {
        'message': 'Task not found'
    }
    return jsonify(msg), 204