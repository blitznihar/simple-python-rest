import pymongo
from bson import Binary, Code
from bson.json_util import dumps, CANONICAL_JSON_OPTIONS

class Customerdb:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["customerdb"]
    mycol = mydb["customers"]
    def insertcustomer(self,customer):
        if customer is None:
            customer = { "name": "John", "address": "Highway 37" }
        return self.mycol.insert_one(customer)
    def getcustomers(self,name):
        filter = {}
        if name is not None:
            filter = { "name": str(name)}
        return dumps(self.mycol.find(filter), json_options=CANONICAL_JSON_OPTIONS)