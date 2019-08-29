import pymongo
import os 

MONGO_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestBD"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGO_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

new_docs = [{'first': 'Neil', 'last': 'Hanslem', 'dob': '14/07/1983', 'gender': 'm', 'hair_colour': 'blonde', 'occupation': 'actor', 'nationality': 'english'}, {'first': 'Rocky', 'last': 'Persolm', 'dob': '19/12/1994', 'gender': 'f', 'hair_colour': 'black', 'occupation': 'activist', 'nationality': 'american'}]
coll.insert_many(new_docs)

documents = coll.find()

for doc in documents:
    print(doc)
    
    