import json

def read_json(filename):
    filepath = "./json/{}".format(filename)
    try:
        with open(filepath, "r") as f:
            data = f.read()
    except FileNotFoundError:
        return {}
    return json.loads(data)
