def chess(num1,num2,pattern):
    x = 0
    for x in range(num2):
        print("")
        
        if x%2 == 0:
            for y in  range(num1):
                print(pattern,end = "")
                x+=1
        else:
            for y in  range(num1):
                print(pattern[::-1],end = "")
                x+=1     
                
    print("\n")
    
print("Welcome to the Chess Pattern.")
answer = "yes"

while True: 
    if answer == "yes":    
        while True:
            pattern = input("Give me only 2 symbols to be your chess pattern: ")
    
            if len(pattern) != 2:
                print("Thats not 2 symbol, give me 2.")
                continue
            else:
                break

        print("Now give me the size of your board: ")
        num1 = int(input("Enter your number: "))
        num2 = int(input("Enter another number: "))

        print("Here is your board: ")

        chess(num1, num2, pattern)
    
    answer = input("Do you want to continue?(yes/no): ").lower()
    if answer == "no":
        print("Good Luck, Bye")
        break
    
    elif answer == "yes":
        print("Ok let's go for another round.")
        
    else: 
        print("Wrong input")
        