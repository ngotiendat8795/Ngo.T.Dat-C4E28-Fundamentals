
from random import randint
from random import choice

q_num = int(input("This is the test of multiplication with 3 multipliers, how many questions do you wanna take?"))
minn = int(input("The smallest number in range for multipliers?"))
maxx = int(input("The largest number in range for multipliers?"))

#--------------- Create questions
count_correct = 0
for i in range (q_num):
    f1 = randint(minn, maxx)
    f2 = randint(minn, maxx)
    f3 = randint(minn, maxx)
    product = f1*f2*f3

    print('Question ', i+1,': The product of',f1,",",f2,"and",f3,"is?")
    
    Matrix = {
        "A" : randint(minn**3, maxx**3),
        "B" : randint(minn**3, maxx**3),
        "C" : randint(minn**3, maxx**3),
        "D" : randint(minn**3, maxx**3),
    }

    #---------ramdomly choose the position of correct answer, then replace the random value created in the maxtrix by correct answer
    answer_list = []
    for key in Matrix.keys():
        answer_list.append(key)

    order = choice(answer_list)
    Matrix[order] = product

    #---------- print the question

    for key, value in Matrix.items():
        print('{}.  {}'.format(key,value))

    #----------Input answer from user
    
    loop = True
    while loop:
        answer = input("Your answer: ").upper()
        if answer in answer_list:
            if product == Matrix[answer]:
                print('''Correct!
                -------------------------''')
                count_correct += 1
            else:
                print('''You're wrong!
                -------------------------''')
            loop = False
        else:
            print('Re-enter your answer in A, B, C or D:')
    

print("You've got",count_correct,"correct out of",q_num,"questions. Congratulation!")
  