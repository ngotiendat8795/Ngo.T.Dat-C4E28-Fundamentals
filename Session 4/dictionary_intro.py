#person = ["Duc",22, 3]

# key: value

person = {
    "name": "Duc",
    "age" : 22,
    "ex" : 3,
    "language": "Chinese"
}

# name = person["name"]
# print(name)

# for key in person.keys():
#     print(key)

# for value in person.values():
#     print(value)

# for key, value in person.items():
#     print(key, value)

#---------------------------------------------------------
# CREATE & UPDATE

# person["city"] = "Hai Phong"
# print(person)

# person["ex"] = 10
# print(person)

#----------------------------------------------------------
#DELETE

del person["ex"]
print(person)