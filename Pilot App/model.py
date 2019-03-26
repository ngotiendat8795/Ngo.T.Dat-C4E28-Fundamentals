import mongodb

database = mongodb.connect()

services = database["services"]

#services la 1 collection trong database