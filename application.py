from flask import Flask, jsonify, request, abort
from stationDAO import stationDAO
from flask_cors import CORS


app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app)
#app = Flask(__name__)

#@app.route('/')
#def index():
#    return "Hello, World!"

#curl "http://127.0.0.1:5000/fuel_stations"
@app.route('/fuel_stations')
def getAll():
    #print("in getall")
    results = stationDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/fuel_stations/2"
@app.route('/fuel_stations/<int:id>')
def findById(id):
    foundStation = stationDAO.findByID(id)

    return jsonify(foundStation)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"station_name\":\"hello\",\"fuel_type_code\":\"someone\",\"zip\":123}" http://127.0.0.1:5000/fuel_stations
@app.route('/fuel_stations', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    fuel_station = {
        "station_name": request.json['station_name'],
        "fuel_type_code": request.json['fuel_type_code'],
        "zip": request.json['zip'],
    }
    values =(fuel_station['station_name'],fuel_station['fuel_type_code'],fuel_station['zip'])
    newId = stationDAO.create(values)
    fuel_station['id'] = newId
    return jsonify(fuel_station)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"station_name\":\"hi\",\"fuel_type_code\":\"nonon\",\"zip\":555}" http://127.0.0.1:5000/fuel_stations/1
@app.route('/fuel_stations/<int:id>', methods=['PUT'])
def update(id):
    foundStation = stationDAO.findByID(id)
    if not foundStation:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'zip' in reqJson and type(reqJson['zip']) is not int:
        abort(400)

    if 'station_name' in reqJson:
        foundStation['station_name'] = reqJson['station_name']
    if 'fuel_type_code' in reqJson:
        foundStation['fuel_type_code'] = reqJson['fuel_type_code']
    if 'zip' in reqJson:
        foundStation['zip'] = reqJson['zip']
    values = (foundStation['station_name'],foundStation['fuel_type_code'],foundStation['zip'],foundStation['id'])
    stationDAO.update(values)
    return jsonify(foundStation)
        

    

@app.route('/fuel_stations/<int:id>' , methods=['DELETE'])
def delete(id):
    stationDAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)