import random

UserScore = 0
ComputerScore = 0
print("Welcome, How many round do you want to play?")
n = input()
m = 0
while m<int(n):
    """ 1 = Rock , 2 = Paper, 3 = Scissor """
    ComputerChoice = random.randint(1,3)
    print("Enter your choice: (rock, papar, scissor)")
    Userchoice = input()
    
    if ComputerChoice == 1 and Userchoice == "rock":
        print("Draw", "Computer choice was:rock ")
        
    elif ComputerChoice == 1 and Userchoice == "paper":
        print("You won", "Computer choice was:rock ")
        UserScore = UserScore + 1
        
    elif ComputerChoice == 1 and Userchoice == "scissor":
        print("You lose" , "Computer choice was:rock ")
        ComputerScore = ComputerScore + 1
        
    elif ComputerChoice == 2 and Userchoice == "rock":
        print("You lose", "Computer choice was:paper ")
        ComputerScore = ComputerScore + 1
        
    elif ComputerChoice == 2 and Userchoice == "paper":
        print("Draw", "Computer choice was:paper ")
        
    elif ComputerChoice == 2 and Userchoice == "scissor":
        print("You won", "Computer choice was:paper ")
        UserScore = UserScore + 1
        
    elif ComputerChoice == 3 and Userchoice == "rock":
        print("You won", "Computer choice was:scissor ")
        UserScore = UserScore + 1
        
    elif ComputerChoice == 3 and Userchoice == "paper":
        print("You lose", "Computer choice was:scissor ")
        ComputerScore = ComputerScore + 1
        
    else: 
        print("Draw", "Computer choice was:scissor ")
        
    m=m+1

print("Your Score is: ", UserScore , " and computer score is: ", ComputerScore,"and the result of the game is: ")

if UserScore > ComputerScore:
    print("You won the game")
elif UserScore < ComputerScore:
    print("You lose the game")
else:
    print("Draw")
    
    
    




    
    