from flask import render_template
from app import app, models

Task = models.Task

# http://www.website.com/
@app.route('/')
def index():
    title = 'My Personal Todo Application!'
    tasks = Task.query.all()
    return render_template("index.html", title=title, tasks=tasks)