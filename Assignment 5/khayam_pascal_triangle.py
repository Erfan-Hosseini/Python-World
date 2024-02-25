def khayam_triangle(size):
    triangle = []
    for i in range(size):
        row = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    for row in triangle:
        print(row)

print("Hello and welcome Khayam pascal triangle creator.")
answer = "yes"  

while True:  
    if answer == "yes":
        size = int(input("Until what sequence do you what the triangle? "))
        khayam_triangle(size)
        
    print("Do you want to see another sequence? ")
    answer = input("yes/no: ").lower()
    
    if answer == "yes":
       print("Ok let's create another triangle")
       
    elif answer == "no":
       print("Good Luck, Bye")
       break
    
    else:
       print("Invalid Input")