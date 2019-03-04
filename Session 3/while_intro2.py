# a = input("Nhap so may muon: ")
# print(len(a))

a = int(input("nhap so: "))
count = 1
while a > 9:
    count = count + 1
    a = a//10
print(count)
