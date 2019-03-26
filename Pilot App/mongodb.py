from pymongo import MongoClient

mongo_uri = "mongodb+srv://admin:admin@cluster0-8tsjf.mongodb.net/test?retryWrites=true"

client = MongoClient(mongo_uri)

def connect():
    db = client.test
    return db

