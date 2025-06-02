""" Level: Beginner
Skills: Lists, file handling, functions

Hint:

Use a list to store tasks.

Create functions like add_task(), view_tasks(), and remove_task().

Use a .txt file to save the tasks persistently. """
#To-Do List App (Console-Based)

storage =[]

def add_task():
    task = input("Add task:\t")
    storage.append(task)

def view_task():
    print(f"task : {storage}")

