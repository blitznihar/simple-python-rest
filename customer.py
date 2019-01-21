from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask.json import jsonify
import customermongo as cs


app = Flask(__name__)
#api = Api(app)
@app.route("/api/v1/customers", defaults={'customername': ""})
@app.route('/api/v1/customers/<customername>', methods=['GET'])
def get(customername):
        cdb = cs.Customerdb()
        if customername == "": customername = None
        result = cdb.getcustomers(customername)
        #for x in result:
            #print(x)
        return jsonify({'customers': result}) # Fetches list of customerids

@app.route('/api/v1/customers', methods=['POST'])
def post():
        customer = request.json
        customerdb = cs.Customerdb()
        #customer = { "name": "Jon Bon", "address": "Highway 39" }
        return jsonify({'customer': str(customerdb.insertcustomer(customer))}) # Fetches list of customerids

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=5008)