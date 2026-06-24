import json
from typing import Any

from objects import Task
from functions import back2_tasks, print_tasks, write_task, read_tasks
import typer

# json file path
file_path = '../../data/data.json'

app = typer.Typer()

@app.command()
def add(task: str, category: str = 'none', priority: int = 3, status: bool = False):
    new_task = Task(task, category, priority, status)
    write_task(new_task, file_path)

@app.command()
def tasks():
    tasks_json = read_tasks(file_path)
    print_tasks(tasks_json)

@app.command()
def complete(task: str):
    with open(file_path, 'r') as file:
        db = json.load(file)

    for i in 0, len(db['tasks']) -1:
        if db['tasks'][i]['name'] == task:
            db['tasks'][i]['status'] = True

    with open(file_path, 'w') as file:
        json.dump(db, file)

if __name__ == '__main__':
    app()