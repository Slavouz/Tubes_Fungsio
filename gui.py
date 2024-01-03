import tkinter as tk

from tkinter import ttk
from app import todo_script, add_task, update_task, delete_task

class TodoApp(ttk.Frame):
    def __init__(self, parent, table_data):        
        super().__init__(master=parent)        

        column_names = ("No.", "Title", "Description")        
        self.table = ttk.Treeview(self, columns=column_names, show='headings')

        # Table Init
        for col in column_names:
            self.table.heading(col, text=col, anchor="w")

        for row in table_data[0:]:
            self.table.insert('', tk.END, values=row)

        self.table.grid(row=0, column=0, sticky=tk.NSEW)
        self.pack(padx=16)                

        # Buttons Frame
        self.button_frame = ttk.Frame(self)
        self.button_frame.grid(row=1, column=0, sticky=tk.EW)
        
        # Buttons Init
        self.add_button = tk.Button(self.button_frame, text="Add", command=lambda: self.show_add_gui())                               
        self.add_button.grid(row=0, column=0, padx=8, pady=16)
        
        self.edit_button = tk.Button(self.button_frame, text="Edit", command=lambda: self.show_edit_gui())                
        self.edit_button.grid(row=0, column=1, padx=8, pady=16)

        self.del_button = tk.Button(self.button_frame, text="Delete", command=lambda: self.show_del_gui())
        self.del_button.grid(row=0, column=2, padx=8, pady=16)        

        todo_script()
    
    def show_add_gui(self):
        add_gui = tk.Toplevel(self)
        add_gui.title("Add New Task")

        title_label = tk.Label(add_gui, text="Task Name:", anchor="w", justify="left")
        title_label.pack(padx=64, pady=16)

        title_input = tk.Entry(add_gui)
        title_input.pack(padx=64)

        desc_label = tk.Label(add_gui, text="Task Description", anchor="w", justify="left")
        desc_label.pack(padx=64, pady=8)

        desc_input = tk.Entry(add_gui)
        desc_input.pack(padx=64)

        add_task_btn = tk.Button(add_gui, text="Add Task", command=lambda:add_task(title_input.get(), desc_input.get(), add_gui, self))
        add_task_btn.pack(padx=64, pady=16)

    def show_edit_gui(self):
        edit_gui = tk.Toplevel(self)
        selected_columns = self.table.selection()
        if len(selected_columns) == 0:
            edit_gui.title("Error")
            tk.Label(edit_gui, text="Kolom yang dipilih kosong").pack()
            tk.Button(edit_gui, text="Ok", command=edit_gui.destroy).pack(pady=8)
        else:
            selected_item = self.table.selection()[0]
            index = self.table.item(selected_item)["values"][0]
            task_val = self.table.item(selected_item)["values"][1]
            desc_val = self.table.item(selected_item)["values"][2]
            edit_gui.title("Edit Task")

            title_label = tk.Label(edit_gui, text="Task Name:", anchor="w", justify="left")
            title_label.pack(padx=64, pady=16)

            title_input = tk.Entry(edit_gui)
            title_input.insert(0, task_val)
            title_input.pack(padx=64)

            desc_label = tk.Label(edit_gui, text="Task Description", anchor="w", justify="left")
            desc_label.pack(padx=64, pady=8)

            desc_input = tk.Entry(edit_gui)
            desc_input.insert(0, desc_val)
            desc_input.pack(padx=64)

            add_task_btn = tk.Button(edit_gui, text="Edit Task", command=lambda:update_task(index, title_input.get(), desc_input.get(), edit_gui, self))
            add_task_btn.pack(padx=64, pady=16)

    def show_del_gui(self):
        del_gui = tk.Toplevel(self)        
        selected_columns = self.table.selection()
        if len(selected_columns) == 0:
            del_gui.title("Error")
            tk.Label(del_gui, text="Kolom yang dipilih kosong").pack(padx=16, pady=16)
            tk.Button(del_gui, text="Ok", command=del_gui.destroy).pack(pady=8)
        else:            
            selected_item = self.table.focus()
            index = self.table.item(selected_item)["values"][0]
            del_gui.title("Confirmation")

            text_label = tk.Label(del_gui, text="Are you sure do you want to delete this task?")
            text_label.pack(padx=16, pady=8)

            button_frame = ttk.Frame(del_gui)
            button_frame.pack(side=tk.BOTTOM, pady=16)

            yes_btn = tk.Button(button_frame, text="Yes", command=lambda:delete_task(index, del_gui, self))
            yes_btn.grid(row=0, column=0, padx=8)

            no_btn = tk.Button(button_frame, text="No", command=lambda:del_gui.destroy())
            no_btn.grid(row=0, column=1, padx=8)
    
if __name__ == "__main__":
    root = tk.Tk()
    root.title('Todo-List App')

    tk.Label(root, text="To-Do List App", font=("Arial", 24, "bold")).pack()
    data = list(todo_script())

    app = TodoApp(root, data)    
    root.mainloop()