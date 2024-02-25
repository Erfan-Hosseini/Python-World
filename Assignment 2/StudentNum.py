print("Welcome, Enter student score(at least 1 score) and if you want to exit, type: exit")
StudentScore = 0
ScoreNumber = 1
while True:
    print("Enter the score of student number ", ScoreNumber)
    Score = input()
    if Score == "exit":
        break
    StudentScore = StudentScore + float(Score)
    ScoreNumber = ScoreNumber + 1
    
print("The average point is: ", StudentScore/(ScoreNumber-1))
    
