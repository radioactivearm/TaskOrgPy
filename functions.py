import json
from objects import Task

def back2_tasks(my_list):
    new_list = []
    for dict in my_list:
        task_obj = Task(
            dict['name'],
            dict['priority'],
            dict['category'],
            dict['status'],
            dict['id']
        )
        new_list.append(task_obj)
    return new_list

# This function takes a json and prints it
def print_json(my_json):
    print(json.dumps(my_json, indent=4))

def print_tasks(my_list):
    my_str = ""
    x = "X"
    obj_list = back2_tasks(my_list)
    highest_len = 0
    # new_list.sort(key=lambda y: y.priority, reverse=False)
    new_list = sorted(obj_list, key=lambda y: (y.priority, y.task), reverse=False)
    for obj in new_list:
        if len(obj.task) > highest_len:
            highest_len = len(obj.task)
    for obj in new_list:
        space_num = 1 + highest_len - len(obj.task)
        space_str = " " * space_num
        if obj.status:
            x = "X"
        else:
            x = " "
        my_str += f"{obj.task}{space_str}[{x}]\n"

    print(my_str)


def write_task(task, file_path):
    task_json = task.to_dict()
    highest_id = 0
    try:
        with open(file_path, 'r') as file:
            db = json.load(file)

        for task in db['tasks']:
            if task['id'] > highest_id:
                highest_id = task['id']
        task_json['id'] = highest_id + 1

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
