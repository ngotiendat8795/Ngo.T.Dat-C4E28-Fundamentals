from model import services
from random import randint, choice

from faker import Faker

name = Faker().name()
adress = Faker().address()


for i in range(50):
    new_service ={
        "name":Faker().name(),
        "age": randint(18,28),
        "gender": choice(["male","female"]),
        "heigh": randint(150,180),
        "address": Faker().address()
    }
    services.insert_one(new_service)
    print("Saved document {0}...".format(i+1))

