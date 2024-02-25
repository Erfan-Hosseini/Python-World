print("Hello and welcome, give me a set of number and i will make it backward for you")
Numbers = int(input("First off, how many number do you want to enter? "))
List = []

for i in range(Numbers):
    print("Enter your", i+1 ,"number: ")
    UserInput = input()
    List.append(UserInput)

"""
With out saving the list and just showing it:
for i in range(Numbers):
    print(List[-i-1],end = " ")
"""

BackList = []

for i in range(Numbers):
    BackList.append(List[-i-1])
    
print("Your original list: ", List)
print("The backward of your list: ", BackList)
