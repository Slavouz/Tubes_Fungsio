import sqlite3

con = sqlite3.connect("todo.db")
cur = con.cursor()

cur.execute("CREATE TABLE todolist(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, desc TEXT)")
print("Success")
con.close()