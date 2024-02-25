print("We want to measure your BMI, please enter your weight(KG) and height(Meter): ")
weight = input("Weight: ")
height = input("Height: ")
bmi = weight / (height*height)

if bmi < 18.5:
    print("You are underweight")
if 18.5<=bmi<25:
    print("You have a normal weight")
if 25<=bmi<30:
    print("You are overweight")
if 30<=bmi<35:
    print("You have obesity")
else:
    print("Watch your self, you have extreme obesity")
    