prices = {
    'banana': 4,
    'apple' : 2,
    'orange': 1.5,
    'pear': 3
}

stock = {
    'banana': 6,
    'apple': 0,
    'orange': 32,
    'pear': 15
}

for key in prices.keys():
    print(key)
    print("price:", prices[key])
    print("stock:", stock[key])
    print(" ")

total = 0

for key in prices.keys():
    value = prices[key] * stock[key]
    print("the value of",key, "is: ", value)
    total = total + value
print("The total value of all stock is: ", total)