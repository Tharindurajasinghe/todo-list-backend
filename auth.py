import json
import os
from tkinter import simpledialog

FILE_NAME = "tasks.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            json.dump({}, f)
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

def login(root):
    username = simpledialog.askstring("Login", "Enter Username:")

    if not username:
        root.destroy()
        exit()

    data = load_data()

    if username not in data:
        data[username] = []
        save_data(data)

    return username, data
