print("Hello and Welcome, give me a set of numbers and i will remove the same one in that set")
print("First off, how many numbers do you want to add?")
Numbers = int(input())
List = []


for i in range(Numbers):
    print("Enter your", i+1 ,"number: ")
    UserInput = input()
    List.append(UserInput)

UniqueNum= []
for num in List:
    if num not in UniqueNum:
        UniqueNum.append(num)
            
print("Your Unique Numebers are: ",UniqueNum)
            
            
    
