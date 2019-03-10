from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes

colors_text= []
colors_index = []
for i in range(len(shapes)):
    block = shapes[i]
    colors_text.append(block["text"])
    colors_index.append(block["color"])
    

def generate_quiz():

    text_display = choice(colors_text)
    color_display = choice(colors_index)

    return [
        text_display,
        color_display,
        randint(0, 1) # 0 : meaning, 1: color
    ]

def mouse_press(x, y, text, color, quiz_type):

    # r1 = range(20,121)
    # r2 = range(140,241)
    # r3 = range(60,161)
    # r4 = range(180,281)

    while loop:
        if x in range(20,121):
            if y in range(60,161):
                color_clicked = "blue"
                loop = false
            elif y in range(180,281):
                color_clicked = "yellow"
                loop = False
            else:
                loop = True

        if x in range(140,241):
            if y in range(60,161):
                color_clicked = "red"
                loop = false
            elif y in range(180,281):
                color_clicked = "green"
                loop = False
            else:
                loop = True 


    if quiz_type == 0: #user have to choose the color based on the meaning
        if color_clicked == text:
            return True
        else: return False

    if quiz_type == 1: #user have to choose the color based on the color

        if colors_text[color_clicked] == colors_index[color]:
            return True
        else: return False





# #Blue   
#     x in range (20,121)
#     y in range (60,161)

# #Red
#     x in range (140,241)
#     y in range (60, 161)

# #Yellow
#     x in range (20,121)
#     y in range (180,281)

# #Green
#     x in range (140,241)
#     y in range (180,281)
