from pymongo import MongoClient
import matplotlib.pyplot as plt 
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_database()

rivers = db["river"]

# #Bai 5

africa_rivers = rivers.find({"continent":'Africa'})
list_africa_river = []
list1_names = []

for river in africa_rivers: 
    list_africa_river.append(river)
    list1_names.append(river['name'])

print(list1_names)

# Bai 6

# samerica_rivers = rivers.find(
#     {"continent":'S. America'},
#     {"length":{"$gte": 1000 }}
# )
# c = samerica_rivers.count()
# print(c)

# list2_names = []
# for river in samerica_rivers:
#     list2_names.append(river['name'])

# print(list2_names)


#------------------------ Duc check ho anh doan code phia tren nay loi gi anh voi nhe
#------------------------------------------------------------------------------------

samerica_rivers = rivers.find(
    {"continent":'S. America'}
)
c = samerica_rivers.count()
print(c)

list2_names = []
for river in samerica_rivers:
    if river['length'] >= 1000:
        list2_names.append(river['name'])
print(list2_names)



