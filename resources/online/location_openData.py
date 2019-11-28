from flask import jsonify, Blueprint
from resources.error_handler import not_found
import requests


locationBP = Blueprint('location', __name__)
openDataURL = 'https://datosabiertos.malaga.eu/recursos/aparcamientos/ubappublicosmun/da_aparcamientosPublicosMunicipales-4326.geojson'


# Search the location of all parkings
@locationBP.route('/local/v1/openData/locations', methods=['GET'])
def searchLocations():
    response = requests.get(openDataURL)
    data = response.json()
    return jsonify(data)

# Search location of a parking (they share the same id)
@locationBP.route('/local/v1/openData/location/<int:loc_id>', methods=['GET'])
def idSearch(loc_id):
    response = requests.get(openDataURL)
    data = response.json()
    if loc_id > 0 and loc_id-1 <= len(data['features']):
        return jsonify(data['features'][loc_id-1])
    else:
        return not_found()


# Search by parking name (return a list of locations)
@locationBP.route('/local/v1/openData/location/<string:name>', methods=['GET'])
def nameSearch(name):
    response = requests.get(openDataURL)
    data = response.json()
    resList = []
    for item in data['features']:
        if name in item['properties']['name']:
            resList.append(item)

    if len(resList) == 0:
        return not_found()
    else:
        return jsonify(resList)


