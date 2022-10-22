from pymongo import MongoClient

MONGO_HOST = "localhost" 
MONGO_PORT = "27017"
MONGO_DB = "db_name"
MONGO_USER = "user_name"
MONGO_PASS = "password"

uri = "mongodb://{}:{}@{}:{}/{}?authSource=admin".format(MONGO_USER, MONGO_PASS, MONGO_HOST, MONGO_PORT, MONGO_DB)
client = MongoClient(uri)
db = client["db_name"]
jobs_collection = db["collection_name"]

objects = [
    {'tenantId': 1001, 'event' : 'first', 'pssi'  : False},
    {'tenantId': 1002, 'event' : 'second', 'pssi'  : False},
    {'tenantId': 1003, 'event' : 'third', 'pssi'  : False},
    {'tenantId': 1004, 'event' : 'fourth', 'pssi'  : False},
    {'tenantId': 1005, 'event' : 'fifth', 'pssi'  : False},
    {'tenantId': 1006, 'event' : 'first', 'pssi'  : False},
    {'tenantId': 1007, 'event' : 'second', 'pssi'  : False},
    {'tenantId': 1008, 'event' : 'third', 'pssi'  : False},
    {'tenantId': 1009, 'event' : 'fourth', 'pssi'  : False},
    {'tenantId': 1010, 'event' : 'fifth', 'pssi'  : False},
    {'tenantId': 1011, 'event' : 'first', 'pssi'  : False},
    {'tenantId': 1012, 'event' : 'second', 'pssi'  : False},
    {'tenantId': 1013, 'event' : 'third', 'pssi'  : False},
    {'tenantId': 1014, 'event' : 'fourth', 'pssi'  : False},
    {'tenantId': 1015, 'event' : 'fifth', 'pssi'  : False},
]
insert = jobs_collection.insert_many(objects)
response = jobs_collection.find({})
print(response)