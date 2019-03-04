flock = [150, 170, 26, 57, 47, 89, 9, 17, 43, 77, 142, 114]

print("Hello my name is Superhero and here is my flock: ", flock)
months = int(input("How long until you sell your flock: "))

for i in range(months):
    print("MONTH", i)
    #Print the stock after 1 month
    for sheep in flock:
        id1 = flock.index(sheep)
        sheep = sheep + 50
        flock[id1] = sheep
    print("One month has passed, now here is my flock: ", flock)

    #Determine the largest sheep
    max = 0
    for sheep in flock:
        if max < sheep:
            max = sheep

    print("Now my biggest sheep has size of ", max, "; Let's shear it")

    #Print the flock after shearing
    id2 = flock.index(max)
    flock[id2] = 8
    print("After shearing, here is my flock: ", flock)
    print("------------------------------------------------------------")

print("After ", months,"months, here is my flock: ", flock)
sum = 0
for sheep in flock:
    sum = sum + sheep
print("My flock has total size of: ", sum)
print("I would get ",sum, " * ","2$ = ",2*sum,"$")