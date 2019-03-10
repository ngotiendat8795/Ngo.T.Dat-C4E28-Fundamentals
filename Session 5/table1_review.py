List_name = []

# Table = {
#     "QUAN" : [25,3,20],
#     "DUC" : [80,5,15]
# }

#JASON

Table = [
    {
        'name' : 'QUAN',
        'money': 25,
        'hour': 3,
        'day': 20
    },
    {
        'name' : 'DUC',
        'money': 80,
        'hour': 5,
        'day': 15
    }
]

# for key in Table.keys():
#     List_name.append(key)

name_input = input("Nhap ten nguoi ban muon kiem tra: ").upper()

for data in Table:
    
    found = False

    count = 0

    if name_input in data.values():
        print(data)
        salary = data["money"] * data["hour"] * data ["day"]
        found = True
        count = count + 1
    
    else:
        found = False

if found:
    print(salary)
else:
    print("There is no data available!")

total = 0
