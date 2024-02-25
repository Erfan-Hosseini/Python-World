print("Welcome to the Snake factory, do you want to have your custom made snake or factory snake? (Custom made price is double) ")
Model = input("(custom/factory): ").lower()

Price = 0

if Model == "factory":
    
    print("(Model 1: *# ), (Model 2: =+ ), (Model 3: KK ), (Model 4: DD ), Model 5: )) )" )
    Answer = int(input("Enter only the model number: "))
    print("Now enter the size of your Snake: ")
    Size = int(input("Enter a number: "))
    
    for i in range(Size):
        if Answer == 1:
            print("*#", end="")
            Price += 1
        
        elif Answer == 2:
            print("=+", end="")
            Price += 1
        
        elif Answer == 3:
            print("KK", end="")
            Price += 1
        
        elif Answer == 4:
            print("DD", end="")
            Price += 1
        
        elif Answer == 5:
            print("))", end="")
            Price += 1
        
        else:
            print("We dont know what model is that, so we go by default model.")
            Answer = 1
            i = 0
    print("--@")

    print("Here is your snake, that comes to: " + str(Price) + "$, enjoy and good bye.")
    
elif Model == "custom": 
    Style = str(input("Give me your idea: "))
    Size = int(input("And now the size of the snake: "))
    for i in range(Size):
        print(Style, end="")
        Price += 2
    print("--@")
    print("Here is your snake, that comes to: " + str(Price) + "$, enjoy and good bye.")
    
else:
    print("Answer correctly next time, Bye")
    
    

