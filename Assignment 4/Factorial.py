print("Hello and welcome to Factorial checker. if you got tired and wanted to stop, enter (Exit).")
List = []

while True:    
    number = input("Enter a number to check if it's a factorial or exit: ").lower()
    if number == "exit":
        print("Ok.")
        break
    number = int(number)

    factorial = 1
    i = 1
    while factorial < number:
        factorial *= i
        i += 1
    if factorial == number:
        check = True
    else:
        check = False

    if check:
        print("Yes, {} is a factorial.".format(number))
    else:
        print("No, {} is not a factorial.".format(number))
        
    List.append(number)
    
x = input("Do you want to know what numbers have you entered?(yes/no)").lower()

if x == "yes":
    print(List)
    print("Bye")
elif x == "no":
    print("Bye")
else:
    print("Wrong input, i take that as a yes")
    print(List)
    print("Bye")
