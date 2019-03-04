# count = 0

# while count < 3:
#     print("hello, how have you been?")
#     # count = count + 1
#     count += 1

# count = 0
# loop = True
# while loop:
#     print("hello ABC")
#     count += 1
#     if count ==2:
#         # loop = False
#         break 
#         print("Bye bye")

from random import randint
i = randint(1,100)
g = int(input("Nhap so du doan: "))
loop = True
count = 0
while loop:
    if count < 7:
        if g > i:
            print("Du doan cao")
            count += 1
            g = int(input("Nhap so du doan: "))
        elif g < i:
            print("Du doan thap")
            g = int(input("Nhap so du doan: "))
            count +=1
        else:
            loop = False
            print(" You're correct")
    else:
        loop = False
        print("Game over!")




