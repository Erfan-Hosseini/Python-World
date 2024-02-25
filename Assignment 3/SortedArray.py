print("Welcome to Array checker, first off, how many numbers do you want to enter?")

Num = int(input("Enter the size of your Array: "))
Answer = "no"

while True:
    if Answer == "no":
        List = []
        for i in range(Num):
            List.append(int(input("Number " + str(i+1) + ": ")))
        print(List)
    Answer = input("Is your list correct? (yes/no): ").lower() 
    if Answer == "yes":
        print("Ok, let's go")
        break
    elif Answer == "no":
        print("Ok lets try again.")
    else:
        print("Invalid input")
        
End = True

SortedList = sorted(List)
if List == SortedList:
    print("Your list is sorted, Good luck, Bye")
    
else:
    print("Your list is not sorted")
    print("Do you want to sort the list? ")
    Answer = input("yes/no: ").lower()
    
    if Answer == "yes":
        print("Here is the sorted list: ", SortedList, ", Good luck, Bye")
    elif Answer == "no":
        print("Good luck, Bye")
    else:
        print("I take that as a yes so here is the sorted list: ", SortedList,", Good luck, Bye")
    
"""
If we don't want to use sorted function:
IsSorted = True
for i in range(1, Num):
    if List[i] < List[i-1]:
        IsSorted = False
        break

if IsSorted:
    print("Your list is sorted")
else:
    print("Your list is not sorted")
"""



    
    

