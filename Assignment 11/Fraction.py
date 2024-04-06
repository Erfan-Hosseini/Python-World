class Fractions:
    #Properties
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    #Methods
    def show(self):
        print(self.numerator, "/", self.denominator)

    def multiply(self,fraction2):
        result_numerator = self.numerator * fraction2.numerator
        result_denominator = self.denominator * fraction2.denominator
        result = Fractions(result_numerator,result_denominator)
        return result

    def sum(self,fraction2):
        result_numerator = self.numerator * fraction2.denominator + fraction2.numerator * self.denominator
        result_denominator = self.denominator *fraction2.denominator
        result = Fractions(result_numerator,result_denominator)
        return result

    def subtraction(self,fraction2):
        result_numerator = fraction1.numerator * fraction2.denominator - fraction2.numerator * fraction1.denominator
        result_denominator = fraction1.denominator * fraction2.denominator
        result = Fractions(result_numerator, result_denominator)
        return result

    def divide(self,fraction2):
        inverted_fraction2 = Fractions(fraction2.denominator, fraction2.numerator)
        result_numerator = self.numerator * inverted_fraction2.numerator
        result_denominator = self.denominator * inverted_fraction2.denominator
        result = Fractions(result_numerator, result_denominator)
        return result


    def fraction_to_number(self):
        result = self.numerator / self.denominator
        return result

#Input function
def inputs():
    a = int(input("Give me the numerator for the first fraction: "))
    b = int(input("Give me the denominator for the first fraction: "))
    fraction1 = Fractions(a,b)
    a = int(input("Give me the numerator for the second fraction: "))
    b = int(input("Give me the denominator for the second fraction: "))
    fraction2 = Fractions(a,b)
    return fraction1, fraction2

#Main  
print("Hello there, select one of the options below: ")

while True:
    print("\n1: combine, 2: subtraction, 3: divide, 4: multiply, 5: simplify, 6: exit")
    answer = input("Give me your choice: ")

    if answer == "1":
       fraction1, fraction2 = inputs()
       answer = fraction1.sum(fraction2)
       answer.show()


    elif answer == "2":
        fraction1, fraction2 = inputs()
        answer = fraction1.subtraction(fraction2)
        answer.show()

    elif answer == "3":
        fraction1, fraction2 = inputs()
        answer = fraction1.divide(fraction2)
        answer.show()

    elif answer == "4":
        fraction1, fraction2 = inputs()
        answer = fraction1.multiply(fraction2)
        answer.show()

    elif answer == "5":
        a = int(input("Give me the numerator: "))
        b = int(input("Give me the denominator: "))
        answer = Fractions(a,b)
        print(answer.fraction_to_number())
        

    elif answer == "6":
        print("Have a good day, Bye.")
        break


    else:
        print("Wrong input.")


