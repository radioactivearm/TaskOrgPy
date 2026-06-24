import json
from objects import Task
from functions import print_json

task1 = Task("Create a Json")
json1 = task1.to_json()

print_json(json1)