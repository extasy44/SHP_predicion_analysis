from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import util

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/get_location_names', methods=['GET'])
@cross_origin()
def get_location_names():
    response = jsonify({
        'suburb': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
@cross_origin()
def predict_home_price():
    data = request.get_json()
    suburb = data['suburb']
    bed = int(data['bed'])    
    bath = int(data['bath'])
    prop_type = int(data['propType'])
    print(data)

    response = jsonify({
        'estimated_price': util.get_estimated_price(suburb,bed,bath,prop_type),
        'data': data
    })

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server...")
    util.load_saved_artifacts()
    app.run()