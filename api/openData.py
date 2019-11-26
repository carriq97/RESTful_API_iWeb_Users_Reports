from flask import jsonify, Blueprint
from api.error_handler import not_found
import requests

openDataBP = Blueprint('openData', __name__)
openDataURL = "https://datosabiertos.malaga.eu/recursos/aparcamientos/ocupappublicosmun/ocupappublicosmunfiware.json"


@openDataBP.route('/api/v1/openData/<int:park_id>')
def idSearch(park_id):
    response = requests.get(openDataURL)
    data = response.json()
    if park_id > 0 and park_id-1 <= len(data):
        return jsonify(data[park_id-1])
    else:
        return not_found


@openDataBP.route('/api/v1/openData/<string:name>')
def nameSearch(name):
    response = requests.get(openDataURL)
    data = response.json()
    for item in data:
        if item['name']['value'] == name:
            return jsonify(item)

    return not_found
