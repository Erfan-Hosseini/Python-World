print("Welcome to (B M M) and (K M M) calculator, enter what you desire: ")

while True:
    
    Answer = input("bmm/kmm/both: ").lower()
    Number1 = int(input("Now enter the first number: "))
    Number2 = int(input("Now enter the second number: "))
    OrginalNumber1 = Number1
    OrginalNumber2 = Number2
    
    if Answer == "bmm" or Answer == "both":
        while Number2 != 0:
            Number3 = Number2
            Number2 = Number1 % Number2
            Number1 = Number3
    
        bmm = Number1
        print("The B M M is:", bmm)

    if Answer == "kmm" or Answer == "both":
        kmm = 1
        Number1 = OrginalNumber1
        Number2 = OrginalNumber2

        if Number1 < 0:
            Number1 = -Number1
        if Number2 < 0:
            Number2 = -Number2

        Number3 = max(Number1, Number2)

        while True:
            if Number3 % Number1 == 0 and Number3 % Number2 == 0:
                kmm = Number3
                break
            Number3 += 1

        print("The K M M is:", kmm)
        
        print("Continue?")
        Answer = input("yes/no: ").lower()
        
        if Answer == "no":
            print("Good luck, Bye")
            break
        elif Answer == "yes":
            print("Ok let's go for another round.")
        else:
            print("I take that as a yes.")
            
