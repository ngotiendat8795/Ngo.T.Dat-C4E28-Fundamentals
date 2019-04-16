from pymongo import MongoClient
from faker import Faker
from random import randint, choice
from bson.objectid import ObjectId


mongo_uri = "mongodb+srv://admin:admin@c4e28cluster-chzuv.mongodb.net/test?retryWrites=true"

# #1. connect
client = MongoClient(mongo_uri)

# #2. get/create database
service_database = client.db_service

# #3. get/create collection
Services = service_database["services"]

# 4. create document, insert document
for i in range(50):
    new_service = {
        "name" : Faker().name(),
        "age" : randint(18,30),
        "Address" : Faker().address(),
        "gender": choice(["male","female"]),
        "available": choice([True, False])
    }
    Services.insert_one(new_service)
    print('Saving document {0} successfully...'.format(i+1))

#5. Read Database
    #5.1. Read All
# all_services = Services.find() #treat this variable as a list #Lady Loading
# for service in all_services:    
   

    #5.2. Read only One
# one_service = services.find_one({ "name":"Mary Strickland" })
# print(one_service)

    #5.2. Read only one with ID
# one_service = Services.find_one({ "_id":ObjectId('5c9a1e066251b45bcccff1dc') })
# print(one_service)

#6. Delete 
# service = Services.find_one({ "_id": ObjectId('5c9a1e0a6251b45bcccff1dd')})
# if service is not None:
#     Services.delete_one(service)
#     print("done")
# else:
#     print("not found")

#7. Update

#-- Find the object u wanna update/manipulate
#-- Create the new value
#-- Consolidated 

one_service = Services.find_one({ "_id": ObjectId('5c9a1e0c6251b45bcccff1e2')})
print(one_service)

new_value = { "$set": {"gender":"female"} }
Services.update_one(one_service,new_value)

