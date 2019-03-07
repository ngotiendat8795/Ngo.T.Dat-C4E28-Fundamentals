strg = input('Input your sentence pls: ')
letters = sorted(list(strg))
statistics = {
}
# print(letters)
a = len(letters)
print(statistics)

for i in range(a):
    j = 0
    # print(letters[i])
    statistics[letters[i]] = 0
    while j < len(letters):
        if letters[i] == letters [j]:
            j += 1
            statistics[letters[i]] += 1
        else: j += 1
        
while " " in statistics:
    del statistics[" "]
    
for key, value in statistics.items():
    print(key, value)