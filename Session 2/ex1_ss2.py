h = int(input("Your height(cm): "))
w = int(input("Your weight: "))
hm = h/100
BMI = w/(hm*hm)

if BMI < 16:
    print("Serverely underweight")
else:
        if BMI < 18.5:
            print("Underweight")
        else:
            if BMI < 25:
                print("Normal")
            else:
                if BMI < 30:
                    print("Overweight")
                else:
                     print("Obsese")

