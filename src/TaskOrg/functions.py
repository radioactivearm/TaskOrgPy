import json
from objects import Task

# This function takes a json and prints it
def print_json(my_json):
    print(json.dumps(my_json, indent=4))


def write_task(task, file_path):
    task_json = task.to_dict()

    try:
        with open(file_path, 'r') as file:
            db = json.load(file)

        db['tasks'].append(task_json)

        with open(file_path, 'w') as file:
            json.dump(db, file, indent=4)
            print("Task appended Successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

def read_tasks(file_path):
    try:
        with open(file_path, 'r') as file:
            db = json.load(file)

        return db['tasks']

    except Exception as e:
        print(f"An error occurred: {e}")
