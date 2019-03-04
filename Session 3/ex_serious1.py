items = ["T-shirt", "Sweater"]
decisions = ["C","R","U","D"]

loop = True
while loop:
    dec = str(input("Welcome to our shop, what do you wanna do: C, R, U, D? "))
    if  dec == "C":
        new_item = str(input("Enter your new item: "))
        items.append(new_item)
        print("Our items: ", *items, sep="; ")
        loop = False

    elif dec == "R":
        print("Our items: ", *items, sep="; ")
        loop = False
    elif dec == "U":
        id = int(input("Enter the position: "))
        new_item = str(input("The update pls: "))
        items[id-1] = new_item
        print("Our items: ", *items, sep=" ")
        loop = False
    elif dec == "D":
        id = int(input("The position pls: "))
        del items[id-1]
        print("Our items: ", *items, sep="; ")
        loop = False
    else:
        print("Input again pls (in the UPPER CASE)")
