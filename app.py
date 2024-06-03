from flask import Flask , render_template , redirect , request , url_for

# create a flask app
app = Flask(__name__)
tasks = []

# home route
@app.route('/')
def index():
    return render_template('index.html' , tasks=tasks)


# define a route for adding tasks
@app.route('/add' , methods=['POST'])
def add_task():
    # task_content = request.form['content']
    task = request.form['task']
    tasks.append(task)
    return redirect(url_for('index'))

# route to delete the added tasks
@app.route('/delete/<int:task_id>' , methods=['POST'])
def delete_task(task_id):
    if task_id < len (tasks):
        del tasks[task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)