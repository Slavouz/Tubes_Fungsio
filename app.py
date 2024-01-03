import sqlite3
import tkinter as tk

def get_connection():
    return sqlite3.connect("todo.db")

def execute_sql(sql, parameters=None):
    connection = sqlite3.connect("todo.db")
    with connection:
        cursor = connection.cursor()
        cursor.execute(sql, parameters)
        return cursor.fetchall()

def refresh_table(todo_app):
    data = list(todo_script())
    todo_app.table.delete(*todo_app.table.get_children())
    for row in data[0:]:
        todo_app.table.insert('', tk.END, values=row)

def todo_script():

    def get_tasks():
        with get_connection() as db:
            return db.execute("SELECT * FROM todolist").fetchall()
            
    # task_list = get_tasks()

    return get_tasks()

def add_task(title, desc, add_gui, todo_app):        
    execute_sql("INSERT INTO todolist (title, desc) VALUES (?, ?)", (title, desc))    
    refresh_table(todo_app)
    # Exit
    add_gui.destroy()
    
def delete_task(index, del_gui, todo_app):    
    print("Deleting task ", index)
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM todolist WHERE id = ?", (index,))
            conn.commit()
    except sqlite3.Error as e:
        print("Error deleting task: ", e)
    # Refresh Table
    refresh_table(todo_app)
    # Exit
    del_gui.destroy()
    
def update_task(index, title, desc, edit_gui, todo_app):    
    execute_sql("""
        UPDATE todolist
        SET title = ?, desc = ?
        WHERE id = ?
    """, (title, desc, index))
    
    # Refresh Table
    refresh_table(todo_app)
    # Exit
    edit_gui.destroy()