import random

print("Hello and welcome to Simple Dice")
NumberOfX = 1
n = 0
Gamecont = "yes"

while True:
    if(Gamecont == "yes"):
        answer = input("Do you want the normal dice or custom dice? (normal/custom): ")
        if answer == "normal" or answer == "custom":
            if answer == "normal":
                x = random.randint(1, 6)
                if x == 6:
                    print("Wow, a six,let's throw another dice")
                    x = random.randint(1, 6)
                    while x == 6:
                        if x == 6:
                            NumberOfX = NumberOfX + 1
                            print("Such luck, you had ", NumberOfX, "of six")
                        else:
                            print("The side was:", x)
                            break
                        x = random.randint(1, 6)
                print("The side was:", x)

            else:
                print("How many side does your dice have and what is the special number?")
                Side = input("Number of sides: ")
                SpecialNum = input("Special Number: ")
                x = random.randint(1, int(Side))
                if x == int(SpecialNum):
                    print("Wow, a", SpecialNum, ", throw another dice")
                    x = random.randint(1, 6)
                    while True:
                        x = random.randint(1, 6)
                        if x == int(SpecialNum):
                            NumberOfX = NumberOfX + 1
                            print("Such luck, you had", NumberOfX, "of", SpecialNum)
                        else:
                            print("The side was: ", x)
                            break
                else:
                    print("The side was: ", x)
        elif answer != "normal" and answer != "custom":
            print("Wrong choice, i don't know what that is, try again.")
    if Gamecont == "yes":
        print("Continue game? (yes/no)")
        Gamecont = input()
    elif Gamecont == "no":
        print("Until later")
        break
    else:
        print("Invalid input, answer only in (yes/no)")
        Gamecont = input()