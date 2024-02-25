def multiplication_table(num1,num2):
    for i in range(1,num1+1):
        print("")
        for j in range(1,num2+1):
            print(i*j, end=" | ")
            
print("Hello and welcome to Multiplication Table creator, i want you to give me 2 numbers and i will give you a multiplication table from 1 to those numbers.")
answer = "yes"

while True:
    if answer == "yes":    
        num1 = int(input("Give me the first number: "))
        num2 = int(input("Now give me the second number: "))

        print("Lets go! Here is your table: ")
        multiplication_table(num1,num2)
        
    print("\n \n Do you want to go again?")
    
    answer = input("(yes/no): ").lower()
    
    if answer == "yes":
        print("Ok let's go for another round.")
        
    elif answer == "no":
        print("Ok, Good Luck, Bye.")
        break
    
    else: 
        print("Invalid Input.")
