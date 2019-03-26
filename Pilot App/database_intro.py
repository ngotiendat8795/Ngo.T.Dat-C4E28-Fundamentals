from pymongo import MongoClient

mongo_uri = "mongodb+srv://admin:admin@cluster0-8tsjf.mongodb.net/test?retryWrites=true"

#connect to database
client = MongoClient(mongo_uri)

# get database
db = client.test

#create collection
games = db["games"]

#create document

new_game = {
    "name":"pikachu",
    "description":"lovely"
}

#insert document

games.insert_one(new_game)

