user = "C4E"
password = "codethechange"
loop = True
while loop:
    user_input = input("Nhap user cua may di cung: ")
    trial_time = 0
    if user_input == user:  
    
       while trial_time < 3:
            password_input = input("Nhap mat khau di cung: ")
            if password_input == password:
                print("WELCOME BABE!")
                loop = False
                break
                
            else:
                print("DM nhap sai roi")
                trial_time = trial_time + 1
          

    else:
        print("Khong tim thay user, nhap lai user di cung ")

