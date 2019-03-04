Dictionary = ["terminology","mitigation","longevity","corporation","implication","policy","lovely"]

from random import randint

#randomely choose a word from the available list

l1 = len(Dictionary)
rd = randint(0,l1-1)
wd = Dictionary[rd]
print(wd)
word_char = list(wd)

#arrange characters of the chosen word in a random order

ran_ord = []
loop = True
while loop:
    rd2 = randint(0,len(word_char)-1)
    ran_ord.append (word_char[rd2])
    del word_char[rd2]
    if len(word_char) == 0:
        loop = False
print(*ran_ord, sep=" ")

#compare the answer

loop2 = True
while loop2:
    answer = str(input("Pls enter your answer: "))

    if answer == wd:
        loop2 = False
        print("You're correct!")
        
    else:
        print("Wrong! Try again")