from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = {'Title': 'Task 1', 'Description': 'Task Description'}

def get_tasks():
    # Fungsi untuk mendapatkan daftar tugas
    return tasks.copy()

def add_task(tasks, new_task):
    # Fungsi untuk menambahkan tugas ke daftar
    new_task = {'Title': request.form.get('task'), 'Description': ''}
    return tasks.copy | {new_task['Title']: new_task}

def delete_task(tasks_list, index):
    # Fungsi untuk menghapus tugas dari daftar berdasarkan indeks
    return tasks_list.copy() - {tasks_list[index]['Title']}

def update_task(tasks, index, updated_task):
    # Fungsi untuk memperbarui tugas dalam daftar berdasarkan indeks
    return tasks.copy() | {updated_task['Title']: updated_task} - {tasks[index]['Title']}

@app.route('/')
def todo_list():
    tasks_list = get_tasks()
    return render_template('todo_list.html', tasks = tasks_list)

@app.route('/add_task', methods=['POST'])
def add_task(tasks):
    tasks = add_task(tasks.copy())
    return redirect('/')

@app.route('/delete_task/<int:index>')
def delete_task(task, index):
    task = delete_task(task = task.copy(), index = index)
    return redirect('/')

@app.route('/update_task/<int:index>', methods=['GET', 'POST'])
def update_task(index):
    if request.method == 'POST':
        updated_task = {'Title': request.form.get('updateTask'), 'Description': ''}
        tasks = update_task(tasks.copy(), index, updated_task)
        return redirect('/')
    else:
        return render_template('update_task.html', index=index, task=tasks[index])


if __name__ == '__main__':
    app.run(debug=True)
