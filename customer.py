from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask.json import jsonify
from flask_cors import CORS, cross_origin

import customermongo as cs


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
#api = Api(app)
@app.route("/api/v1/customers", defaults={'customername': ""})
@app.route('/api/v1/customers/<customername>', methods=['GET'])
@cross_origin()
def get(customername):
        cdb = cs.Customerdb()
        if customername == "": customername = None
        result = cdb.getcustomers(customername)
        #for x in result:
            #print(x)
        return jsonify(result) # Fetches list of customerids

@app.route('/api/v1/customers', methods=['POST'])
@cross_origin()
def post():
        customer = request.json
        customerdb = cs.Customerdb()
        #customer = { "name": "Jon Bon", "address": "Highway 39" }
        return jsonify({'customer': str(customerdb.insertcustomer(customer))}) # Fetches list of customerids

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=5008)