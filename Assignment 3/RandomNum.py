import random

print("Welcome to random number generator, first of all, how many random number do you want to generate?")
RandomNum = int(input("Enter a number: "))
First = 0
Last = 100
ListOfNum = []
print("Do you want to change the range of random numbers? (Default is between 0 and 100) (yes/no)")
Answer = input().lower()
if Answer == "yes":
    First = int(input("Start from: "))
    Last = int(input("End to: "))
elif Answer == "no":
    print("As you please")
else:
    print("I dont know what that is, so let's go by default")

for i in range(RandomNum):
    ListOfNum.append(random.randint(First, Last))
    
print(ListOfNum)

while True:
    print("Add or remove number?")
    Answer = input("add/remove/exit: ").lower()
    
    if Answer == "add":
        Answer = input("Add a random number or do you want to input something? (random/input): ").lower()
        
        if Answer == "random":
            ListOfNum.append(random.randint(First, Last))
            print(ListOfNum)
            
        elif Answer == "input":
            UserNum = int(input("Enter your number: "))
            ListOfNum.append(UserNum)
            print(ListOfNum)
            
        else:
            print("Invalid input")
            
    elif Answer == "remove":    
            Answer = input("Remove the last number or the number you enter or random number? (last/input/random): ")
            if Answer == "last":
                ListOfNum.pop(-1)
                print(ListOfNum)
                
            elif Answer == "input":
                UserNum = int(input("Enter your number: "))
                ListOfNum.remove(UserNum)
                print(ListOfNum)
                
            elif Answer == "random":
                x = random.randint(0, len(ListOfNum)-1)
                ListOfNum.pop(x)
                print(ListOfNum)
                
            else:
                print("Invalid input")
                
    elif Answer == "exit":
        print("Good luck mate, Bye")
        break
                
    else:
        print("Invalid input")
    
        