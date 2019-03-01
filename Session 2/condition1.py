# yob= int(input("Enter your yob:"))
# # x = datetime.now
# age = 2019 - yob

# if age < 10:
#     print("babe cachima stay here with me cachima")
# elif age < 18
#     print("olala")
# else:
#     print("This is not for fun")

# from random import randint
# i = randint(1,1000)
# if i < 35:
#     print("sunny")
# elif i <70:
#     print("Rainy")
# else
#     print("sexy")


# print("Your equation is: ax^2 + bx + c = 0")
# a = int(input("enter a:"))
# b = int(input("enter b:"))
# c = int(input("enetr c:"))
# delta = b*b - 4*a*c
# if delta < 0:
#     print("The equation has no solution")
# elif delta == 0:
#     print("the equation has only one root")
# else:
#     print("the equation has two roots")

m = int(input("nhap so dau"))
n = int(input("nhap so cuoi"))
for i in range(m,n+1):
    remainder = i % 2
    if remainder == 0:
        print(i)