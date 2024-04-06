class ComplexNumber:

    #Properties
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    #Methods
    def add(self, other):
        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def multiply(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imaginary_part)

    def subtract(self, other):
        real_part = self.real - other.real
        imaginary_part = self.imaginary - other.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def display(self):
        return f"{self.real} + {self.imaginary}i"

#Function
def inputs():
    num1_real = float(input("Enter the real part of the first complex number: "))
    num1_imaginary = float(input("Enter the imaginary part of the first complex number: "))
    num2_real = float(input("Enter the real part of the second complex number: "))
    num2_imaginary = float(input("Enter the imaginary part of the second complex number: "))
    num1 = ComplexNumber(num1_real, num1_imaginary)
    num2 = ComplexNumber(num2_real, num2_imaginary)
    return num1,num2

#main
while True:
    print("\n1: combine, 2: subtraction, 3: multiply, 4: exit")
    choice = input("Give me your choice: ")

    if choice == '1':
        num1,num2 = inputs()
        result = num1.add(num2)
        print("Result:", result.display())

    elif choice == '2':
        num1,num2 = inputs()
        result = num1.subtract(num2)
        print("Result:", result.display())

    elif choice == '3':
        num1,num2 = inputs()
        result = num1.multiply(num2)
        print("Result:", result.display())

    elif choice == '4':
        print("Good Luck, Bye.")
        break

    else:
        print("Invalid input")


