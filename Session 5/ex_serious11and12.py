def is_inside(a,b):
    # a= [x1,y1]
    # b= [x2,y2,w,h]
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    w = b[2]
    h = b[3]

    if x1 in range(x2,x2+h):
        if y1 in range(y2, y2+w):
            return True
        else: return False
    else: return False
    
if is_inside([100,100],[50,50,100,100]) == True:
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
