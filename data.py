import json


def read_json(file_name="game_data.json"):
    try:
        with open(file_name, "r", encoding='utf-8') as file:
            return json.load(file)
    except:
        return {}


def write_json(data, file_name="user_data.json"):
    with open(file_name, "w") as file:
        json.dump(data, file)
