import math

print("Hello and Welcome to the simple calculator, Please select your choice:")
print("+,-,*,/,sin,cos,tan,cot,sqrt,pow,fac,log")
op = input()

if op == "+" or op == "-" or op == "*" or op == "/":
    num1 = float(input("Enter your first Number: "))
    num2 = float(input("Enter your Second Number: "))
else:
    num1 = float(input("Enter your Number: "))
    
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
elif op == "sin":
    print(math.sin(num1))
elif op == "cos":
    print(math.cos(num1))
elif op == "tan":
    print(math.tan(num1))
elif op == "cot":
    print(math.cos(num1)/math.sin(num1))
elif op == "sqrt":
    print(math.sqrt(num1))
elif op == "pow":
    print(num1*num1)
elif op == "fac":
    print(math.factorial(num1))
elif op == "log":
    print(math.log(num1))
    
    
    