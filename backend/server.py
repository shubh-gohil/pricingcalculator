from flask import Flask
from flask import request
from utils import read_json

app = Flask(__name__)


@app.route("/hyperscalars")
def get_hyperscalars():
    """Get list of all available GenAI model providers"""

    data = read_json("hyperscalars.json")
    print(data)
    return data["hyperscalars"]


# @app.route("/models/<int:hyperscalar_id>")
# def get_model_names(hyperscalar_id):
#     data = read_json("models.json")
#     names = []

#     for model in data["models"]:
#         if hyperscalar_id == model["hyperscalar_id"]:
#             model_info = model["model_info"]
#             break
    
#     if not model_info:
#         return {"model_name": "No model available with the model_id {}".format(hyperscalar_id)}
    
#     for model_name in model_info:
#         names.append(model_name["name"])

#     return names


@app.route("/models/<int:hyperscalar_id>")
def get_all_models_and_info(hyperscalar_id):
    """Get list of all models available of a particular provider"""

    data = read_json("models.json")

    for model in data["models"]:
        if hyperscalar_id == model["hyperscalar_id"]:
            model_info = model["model_info"]
            return model_info


@app.route("/model_info/<int:model_id>")
def get_model_info(model_id):
    """Get information about a particular model"""

    data = read_json("models.json")

    for model in data["models"]:
        if model_id == model["model_id"]:
            model_info = model["model_info"]


@app.route("/cost")
def get_infra_cost():
    """Get the infrastructure cost of all the hyperscalars"""
    
    data = read_json("infra_cost.json")

    return data["hyperscalars"]


if __name__ == "__main__":
    app.run(debug=True)