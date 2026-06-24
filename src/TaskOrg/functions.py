import json

# This function takes a json and prints it
def print_json(my_json):
    print(json.dumps(my_json, indent=4))