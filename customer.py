from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask.json import jsonify


app = Flask(__name__)
api = Api(app)

class Customers(Resource):
    def get(self):
        list = ((1,2,3,4,5,6,7))
        return {'customers': list} # Fetches list of customerids
        

api.add_resource(Customers, '/customers') # Route_1


if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')