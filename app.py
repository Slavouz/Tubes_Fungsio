import sqlite3
import tkinter as tk

def todo_script():

    def get_tasks():
        con = sqlite3.connect("todo.db")
        cur = con.cursor()
        # Fungsi untuk mendapatkan daftar tugas
        return cur.execute("SELECT * FROM todolist").fetchall()    
            
    task_list = get_tasks()

    return list(task_list)

def add_task(title, desc, add_gui, todo_app):
    # Fungsi untuk menambahkan tugas ke daftar
    con = sqlite3.connect("todo.db")
    cur = con.cursor()    
    cur.execute("INSERT INTO todolist (title, desc) VALUES (?, ?)", (title, desc))
    con.commit()
    # Refresh Table
    data = todo_script()
    todo_app.table.delete(*todo_app.table.get_children())
    for row in data[0:]:
        todo_app.table.insert('', tk.END, values=row)        
    # Exit
    add_gui.destroy()
    
def delete_task(index, del_gui, todo_app):
    # Fungsi untuk menghapus tugas dari daftar berdasarkan indeks
    con = sqlite3.connect("todo.db")
    cur = con.cursor()    
    cur.execute("DELETE FROM todolist WHERE id = ?", (index,))
    con.commit()
    # Refresh Table
    data = todo_script()
    todo_app.table.delete(*todo_app.table.get_children())
    for row in data[0:]:
        todo_app.table.insert('', tk.END, values=row)
    # Exit
    del_gui.destroy()
    
def update_task(index, title, desc, edit_gui, todo_app):
    # Fungsi untuk memperbarui tugas dalam daftar berdasarkan indeks
    con = sqlite3.connect("todo.db")
    cur = con.cursor()        
    cur.execute("""
        UPDATE todolist
        SET title = ?, desc = ?
        WHERE id = ?
    """, (title, desc, index))
    con.commit()
    # Refresh Table
    data = todo_script()
    todo_app.table.delete(*todo_app.table.get_children())
    for row in data[0:]:
        todo_app.table.insert('', tk.END, values=row)        
    # Exit
    edit_gui.destroy()