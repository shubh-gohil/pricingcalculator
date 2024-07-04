def read_json(filename):
    filepath = "json/".join(filename)
    try:
        with open(filepath, "r") as f:
            data = f.read()
    except FileNotFoundError:
        return {}
    return data
