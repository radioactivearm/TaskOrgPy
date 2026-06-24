import json
from objects import Task
from functions import print_json, write_task, read_tasks
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
    print_json(tasks_json)

if __name__ == '__main__':
    app()