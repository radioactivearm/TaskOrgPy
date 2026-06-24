import json
from typing import Any

from objects import Task
from functions import print_tasks, write_task, read_tasks
import typer



app = typer.Typer()

# add command adds a task to the json file
@app.command()
def add(task: str, priority: int, category: str = 'none', status: bool = False):
    new_task = Task(task, priority, category, status)
    write_task(new_task, file_path)

# tasks command lists out the current tasks
@app.command()
def tasks():
    tasks_json = read_tasks(file_path)
    print_tasks(tasks_json)

# a command to change the status of task to True
@app.command()
def complete(task: str):
    with open(file_path, 'r') as file:
        db = json.load(file)

    for i in 0, len(db['tasks']) -1:
        if db['tasks'][i]['name'] == task:
            db['tasks'][i]['status'] = True

    with open(file_path, 'w') as file:
        json.dump(db, file)

@app.command()
def change_priority(task: str, priority: int):
    with open(file_path, 'r') as file:
        db = json.load(file)

    for i in range(0, len(db['tasks'])):
        if db['tasks'][i]['name'] == task:
            db['tasks'][i]['priority'] = priority

    with open(file_path, 'w') as file:
        json.dump(db, file)

@app.command()
def init():
    db = {'User': username, 'tasks': []}
    try:
        with open(file_path, 'w') as file:
            json.dump(db, file, indent=4)
        print("Structure Loaded")
    except Exception as e:
        print(f"An error occurred: {e}")


@app.command()
def clear():
    with open(file_path, 'r') as file:
        db = json.load(file)

    for i in range(0, len(db['tasks'])):
        if db['tasks'][i]['status']:
            db['tasks'].pop(i)

    with open(file_path, 'w') as file:
        json.dump(db, file)


@app.command()
def clear_all():
    with open(file_path, 'r') as file:
        db = json.load(file)

    for i in range(0, len(db['tasks'])):
        db['tasks'].pop()

    with open(file_path, 'w') as file:
        json.dump(db, file)


if __name__ == '__main__':
    app()