import math  

def tertiary_equation(a, b, c, d):
    delta_0 = b ** 2 - 3 * a * c
    delta_1 = 2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d
    delta = (delta_1 ** 2 - 4 * delta_0 ** 3)
   

    if delta > 0:  
        u1 = 1
        u2 = (-1 + math.sqrt(3) * 1j) / 2
        u3 = (-1 - math.sqrt(3) * 1j) / 2

        C = ((delta_1 + math.sqrt(delta)) / 2) ** (1 / 3)
        x1 = (-1 / (3 * a)) * (b + u1 * C + delta_0 / (u1 * C))
        x2 = (-1 / (3 * a)) * (b + u2 * C + delta_0 / (u2 * C))
        x3 = (-1 / (3 * a)) * (b + u3 * C + delta_0 / (u3 * C))
        
        return x1, x2, x3

    elif delta == 0: 
        if delta_0 == 0:  
            x = -b / (3 * a)
            return x, x, x
        else:
            K = -delta_1 / (delta_0 * 2)
            x1 = -b / (3 * a) + K
            x2 = -(b + K * a) / 2
            x3 = math.sqrt(3) * (b - K * a) / 2j
            return x1, x2, x3

    else:  
        K = (delta_1 + math.sqrt(delta)) / 2
        x1 = (K / (2 * delta_0)) ** (1 / 3)
        x2 = (-b - x1 * (delta_0 / K)) / (3 * a)
        x3 = (-b + x1 * (1 + 0.5j * math.sqrt(3)) * (delta_0 / K)) / (3 * a)
        return x1, x2, x3



answer = "yes"

print("Welcome to the Tertiary Equation, give me the a,b,c,d for the equation below and i will give you the answer.")

while True:
    if answer == "yes":
        print("ax^3+bx^2+cx+d=0")
        a = int(input("Give me the a: "))
        b = int(input("Give me the b: "))
        c = int(input("Give me the c: "))
        d = int(input("Give me the d: "))       
        print("The roots are: ",tertiary_equation(a,b,c,d))   
        
    answer = input("Go another round?(yes/no)").lower()
    
    if answer == "yes":
        print("Ok let's go!")
    elif answer == "no":
        print("Good luck, Bye.")
        break
    else:
        print("Invalid input.")
        
    
        