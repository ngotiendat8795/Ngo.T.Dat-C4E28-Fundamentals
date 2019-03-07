# a = 50

# # print("think about your number between 1 and 100"
# print("may dang nghi den")
# print(a)
# b = input("ah:")

# python 3 format

# while True:
#     if b == "c":
#         print("Chuan vl")
#         break

#     else:
#         if b == "l":
#             a = (100-a)//2
#             print("the",a, end =" ")
#             input("co phai khong?")
#         else:
#             a = (a-1)//2
#             print("the",a)
#             input("co phai khong?")

#----------------------------------

print('''
aaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaa
''')
low = 1
high = 100

while True:
    mid = (low + high)//2
    answer_input = input("is {0} your number?".format(mid))

    if answer_input == 'c':
        print("I knew it")
        break
    elif answer_input == 's':
        high = mid
    else:
        low = mid