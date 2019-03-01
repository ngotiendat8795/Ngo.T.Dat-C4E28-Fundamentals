n = int(input("Nhap so muon tinh giai thua: "))
fac = 1
if n == 0 :
    print("Giai thua cua 0 bang 1")
else:
    for i in range (1,n+1):
        fac = fac * i
    print("Giai thua cua ",n," la ",fac)
