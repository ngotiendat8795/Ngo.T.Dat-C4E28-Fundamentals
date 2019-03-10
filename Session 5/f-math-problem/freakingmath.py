from random import *
# from random import choice


x = randint(1,10)
y = randint(1,10)

Matrix = {
    "+" : x+y,
    "-" : x-y,
    "*" : x*y,
    "/": x/y
}
list_op = []
for key in Matrix.keys():
    list_op.append(key)
    

op = choice(list_op)
error = choice([0,1,2,0,1,2])
crr_asw = Matrix[op]
result = crr_asw + error

def generate_quiz():

    # Hint: Return [x, y, op, result]
    return [x,y,op,result]

def check_answer(x, y, op, result, user_choice):
    if error == 0:
        if user_choice == True:
            return True
        else: return False
    else:
        if user_choice == True:
            return False
        else:
            return True
