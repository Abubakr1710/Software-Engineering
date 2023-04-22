from flask import Flask, render_template, request, redirect # Import the Flask class from the flask module
from flask_sqlalchemy import SQLAlchemy # Import the SQLAlchemy class from the flask_sqlalchemy module
from datetime import datetime # Import the datetime class from the datetime module

app = Flask(__name__) # Global variable __name__ tells Flask whether or not we are running the file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # Relative path to the database file
db = SQLAlchemy(app) # Create a database instance

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True) # The id of the task
    content = db.Column(db.String(200), nullable=False) # The content of the task
    #completed = db.Column(db.Integer, default=0) # The status of the task (0 = incomplete, 1 = complete)
    date_created = db.Column(db.DateTime, default=datetime.utcnow) # The date the task was created

    def __repr__(self): # This is how we will see the task when we query the database
        return '<Task %r>' % self.id # This is how we will see the task when we query the database

@app.route('/', methods=['POST', 'GET']) # The "@" symbol designates a "decorator" which attaches the following function to the '/' route. This means that whenever we send a request to localhost:5000/ we will run the following "hello_world" function.
def index():
    if request.method == 'POST': # If the request method is POST, then we want to add a new task to the database
        task_content = request.form['content'] # Get the task content from the form
        new_task = Todo(content=task_content) # Create a new task object

        try: # Try to add the new task to the database
            db.session.add(new_task) # Add the new task to the database
            db.session.commit() # Commit the changes
            return redirect('/') # Redirect the user to the home page
        except: # If there is an error, print it to the terminal
            return 'There was an issue adding your task' # If there was an error, return this message
    else: # If the request method is GET, then we want to get all the tasks from the database and display them on the home page
        tasks = Todo.query.order_by(Todo.date_created).all() # Get all the tasks from the database and order them by date created 
        return render_template("index.html", tasks=tasks) # Render the template and return it!

@app.route('/delete/<int:id>') # The "<int:id>" part of the route is a variable that will be passed in when we call the route
def delete(id): # The "id" variable will be the id of the task we want to delete
    task_to_delete = Todo.query.get_or_404(id) # Get the task with the id that was passed in

    try:
        db.session.delete(task_to_delete) # Delete the task
        db.session.commit() # Commit the changes
        return redirect('/') # Redirect to the home page
    except:
        return 'There was a problem deleting that task' # If there was an error, return this message

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id) # Get the task with the id that was passed in

    if request.method == 'POST': # If the request method is POST, then we want to update the task in the database
        task.content = request.form['content'] # Get the task content from the form  

        try:
            db.session.commit() # Commit the changes
            return redirect('/') # Redirect to the home page
        except:
            return 'There was an issue updating your task'
    else: # If the request method is GET, then we want to display the task on the update page
        return render_template("update.html", task=task) # Render the template and return it!


if __name__ == "__main__": # Ensure this file is being run directly and not from a different module
    app.run(debug=True) # Run the app in debug mode.
