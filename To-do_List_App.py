# To-do List with GUI

from tkinter import *

window = Tk()
window.title("To-do List")

task= []

# Functions

def remove_task(task, variable):
    if variable.get() == 1:
        task.destroy()

def add_task():

    task_text = new_task.get()

    if task_text != "Add New Task" and task_text != "":
        var = IntVar()
        task_list = Checkbutton(window, font = ("Roboto", 16), 
                                text = task_text, variable = var)
        
        task_list.config(command = lambda: remove_task(task_list, var))

        task_list.pack(anchor = "w")

        new_task.delete(0, END)

# To add a new task

new_task = Entry(window, font= ("Roboto", 16))

new_task.insert(0, "Add New task")
new_task.pack()

# Submit Button

submit_button = Button(window, text = "Submit",
                       font = ("Roboto", 16),
                       command = add_task)

submit_button.pack(anchor = "e")

window.mainloop()