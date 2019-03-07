from random import choice 
rd_list = []
word = 'champion'
list_word = list(word)
print(choice(word))

while len(list_word) > 0:
    char = choice(list_word)
    rd_list.append(char)
    list_word.remove(char)  #cach thu 3 de xoa 1 phan tu ngoai pop va del


print(*rd_list, sep=" ")

while True:
    user_word = input("Your word pls: ")
    if user_word == word:
        print("Dm chuan roi")
        break
    else:
        print("Sai roi babe")



