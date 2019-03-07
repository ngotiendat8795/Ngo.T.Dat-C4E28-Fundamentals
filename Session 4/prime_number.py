pn = int(input("Enter your number: "))
nf = 0

for i in range (1,pn+1):
    if pn % i == 0:
        nf = nf + 1

if nf == 2:
    print("This is a prime number.")
else:
    print("This is not a prime number.")



# #Tao bien trang thai
# its_prime = True

# if nf == 2:
#     its_prime = True
# else:
#     its_prime = False


#Dung While instead of for
# while i < n:
    if n % i ==0 :
        its_prime 