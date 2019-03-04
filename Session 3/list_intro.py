#list/array
#CRUD creat read update delete

# menu = ["COM", "PHO", "BUN DAU", "MAM TOM"]
# print(" Nha tao co những món sau:", *menu,sep=",  ")
# a = input("May muon an them cai gì: ")
# menu.append (a)

# print(*menu,sep='\n')

menu = ["COM", "PHO", "BUN DAU", "MAM TOM"]
# count = 0
# a = menu[-1]
# id = menu.index(a)
# while count < (id+1):
#     print(count+1,". ",menu[count])
#     count=count+1

# print(*menu,sep='\n')

#Loop with item-----------------------------------------------
# for item in menu:
#     print(item)

#Loop with index-----------------------------------------------
# for index in range(len(menu)):
#     print(index)

#Loop with both item and index-------------------------------------

# for index, item in enumerate(menu):
#     print(index+1, item)

#Update------------------------------------------

# for index, item in enumerate(menu):
#     print(index+1, item)

# a = int(input("where do you want to update: "))
# b = input("Your update pls: ")
# menu[a-1] = b

# for index, item in enumerate(menu):
#     print(index+1, item)


#DELETE-----------------------------------------------------
#1
# menu.pop(1)
# for index, item in enumerate(menu):
#     print(index+1, item)

#2

for index, item in enumerate(menu):
    print(index+1, item)
    print('-------------------------------------------')
a = int(input("where to delete: "))
del menu[a-1]
for index, item in enumerate(menu):
    print(index+1, item)
    print('-------------------------------------------')

