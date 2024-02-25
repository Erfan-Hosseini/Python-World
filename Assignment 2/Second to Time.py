print("Welcome, How many seconds do you want to count?")
seconds = input()
seconds = float(seconds) 
hour = seconds // 3600
seconds = seconds -(hour*3600)
minute = seconds // 60
seconds = seconds -(minute*60)

print("You have ",hour," Hour and ", minute," Minute and", seconds,"Second" )