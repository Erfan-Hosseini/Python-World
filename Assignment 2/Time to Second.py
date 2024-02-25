print("Welcome, Answer the following questions: ")
print("How many Hour?")
hour = input()
print("How many Minute?")
minute = input()
print("How many Second?")
second = input()

print("Do you want to add days?(y/n)")
question = input()

if question == "y":
    print("Enter the number of days")
    day = input()
else:
    day = 0
    
seconds = int(second) + (int(minute)*60) + (int(hour)*3600) +(int(day)*86400)

print("The number of seconds in your inpur is: ", seconds)
