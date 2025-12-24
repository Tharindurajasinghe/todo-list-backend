import tkinter as tk
from tkinter import messagebox
from auth import login, save_data

# -------------------- APP WINDOW --------------------
root = tk.Tk()
root.title("To-Do List App")
root.geometry("700x500")

# -------------------- LOGIN --------------------
username, data = login(root)

# -------------------- FUNCTIONS --------------------
def refresh_list():
    task_list.delete(0, tk.END)
    for task in data[username]:
        display = f"{task['name']} | {task['priority']} | {task['due']} | {task['category']} | {task['status']}"
        task_list.insert(tk.END, display)

def add_task():
    if task_name.get() == "":
        messagebox.showerror("Error", "Task name required")
        return

    task = {
        "name": task_name.get(),
        "priority": priority.get(),
        "due": due_date.get(),
        "category": category.get(),
        "status": "Pending"
    }

    data[username].append(task)
    save_data(data)
    refresh_list()
    clear_fields()

def delete_task():
    try:
        index = task_list.curselection()[0]
        data[username].pop(index)
        save_data(data)
        refresh_list()
    except:
        messagebox.showerror("Error", "Select a task")

def complete_task():
    try:
        index = task_list.curselection()[0]
        data[username][index]["status"] = "Completed"
        save_data(data)
        refresh_list()
    except:
        messagebox.showerror("Error", "Select a task")

def edit_task():
    try:
        index = task_list.curselection()[0]
        task = data[username][index]

        task["name"] = task_name.get()
        task["priority"] = priority.get()
        task["due"] = due_date.get()
        task["category"] = category.get()

        save_data(data)
        refresh_list()
        clear_fields()
    except:
        messagebox.showerror("Error", "Select a task")

def load_selected(event):
    try:
        index = task_list.curselection()[0]
        task = data[username][index]

        task_name.set(task["name"])
        priority.set(task["priority"])
        due_date.set(task["due"])
        category.set(task["category"])
    except:
        pass

def clear_fields():
    task_name.set("")
    priority.set("Low")
    due_date.set("")
    category.set("")

# -------------------- UI --------------------
tk.Label(root, text=f"Welcome {username}", font=("Arial", 14)).pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=10)

task_name = tk.StringVar()
priority = tk.StringVar(value="Low")
due_date = tk.StringVar()
category = tk.StringVar()

tk.Label(frame, text="Task Name").grid(row=0, column=0)
tk.Entry(frame, textvariable=task_name).grid(row=0, column=1)

tk.Label(frame, text="Priority").grid(row=1, column=0)
tk.OptionMenu(frame, priority, "High", "Low").grid(row=1, column=1)

tk.Label(frame, text="Due Date").grid(row=2, column=0)
tk.Entry(frame, textvariable=due_date).grid(row=2, column=1)

tk.Label(frame, text="Category").grid(row=3, column=0)
tk.Entry(frame, textvariable=category).grid(row=3, column=1)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Task", command=add_task).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Edit Task", command=edit_task).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete Task", command=delete_task).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Complete Task", command=complete_task).grid(row=0, column=3, padx=5)

task_list = tk.Listbox(root, width=90)
task_list.pack(pady=10)
task_list.bind("<<ListboxSelect>>", load_selected)

refresh_list()
root.mainloop()

