print("Hello there, please enter your first and last name: ")
name = input()

print("Good, and now enter your grades: ")

a = int(input())
b = int(input())
c = int(input())

if ((a+b+c)/3)>=17:
    print("Well done", name)
elif 12<=((a+b+c)/3)<17:
    print("You are doing fine", name)
else:
    print("You need to work harder: ", name)
print("The average of your score is: ",(a+b+c)/3)
    