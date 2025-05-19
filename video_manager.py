import json

def load_data(videaos):
    try: 
        with open('data.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('data.txt', 'w') as file:
            return json.dump(videos, file)