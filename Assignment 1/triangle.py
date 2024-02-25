print("Enter the 3 sizes of triangle's side: ")
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if a+b<c or a+c<b or b+c<a:
    print("This 3 numbers wont make a triangle.")
else: 
    print("Nice")
    