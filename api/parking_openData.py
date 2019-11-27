from flask import jsonify, Blueprint
from api.error_handler import not_found
import requests

parkingBP = Blueprint('parking', __name__)
openDataURL = 'https://datosabiertos.malaga.eu/recursos/aparcamientos/ocupappublicosmun/ocupappublicosmunfiware.json'

# Search all the parkings
@parkingBP.route('/api/v1/openData/parkings', methods=['GET'])
def parkingsSearch():
    response = requests.get(openDataURL)
    data = response.json()
    return jsonify(data)


# Search by parking id
@parkingBP.route('/api/v1/openData/parking/<int:park_id>', methods=['GET'])
def idSearch(park_id):
    response = requests.get(openDataURL)
    data = response.json()
    if park_id > 0 and park_id-1 <= len(data):
        return jsonify(data[park_id-1])
    else:
        return not_found()


# Search by parking name (return a list of parkings)
@parkingBP.route('/api/v1/openData/parking/<string:name>', methods=['GET'])
def nameSearch(name):
    response = requests.get(openDataURL)
    data = response.json()
    resList = []
    for item in data:
        if name in item['name']['value']:
            resList.append(item)

    if len(resList) == 0:
        return not_found()
    else:
        return jsonify(resList)
