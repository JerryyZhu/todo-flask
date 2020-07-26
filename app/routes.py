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
