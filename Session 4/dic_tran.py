diction = {
    "love": "yeu",
    "run": "chay",
    "go": "di",
    "fly": "bay"
}

for word in diction.keys():
    print(word, end=" ")

word_input = input("Enter your word: ")
if word_input in diction.keys(): #or word in diction: 
    print(diction[word_input])
else:
    answer = input("your word is not available, do you wanna add, Y or N?").upper()
    if answer ==  "Y":
        mean = input("Enter the meaning: ")
        diction[word_input] = mean
        print(diction)

    else:
        exit()
        