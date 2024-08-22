import json

def read_bot_manifest(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)