import qrcode

print("Welcome to the simple QRCode creator, first off, tell me what do you want to add in your QRCode?")
print("The options are: First name(Fname), Last name(Lname), Telephone number(Tnum), National code(Ncode), Email(Email)")
print("Country(Country), Address(Address), Extra information(Extra), and if you want to exit, enter (Exit)")
information = []
UserInput = []

while True:
    Input = input("What do you want to enter? ").lower()
    
    if Input in UserInput:
        print("I already have that information")
        continue
    
    elif Input == "exit":
        break
    
    elif Input == "fname":
        x = input("What is your first name? ")
        information.append(x)
        UserInput.append("fname")
    
    elif Input == "lname":
        x = input("What is your last name? ")
        information.append(x)
        UserInput.append("lname")
        
    elif Input == "tnum":
        x = input("What is your Telephone Number? ")
        information.append(x)
        UserInput.append("tnum")
        
    elif Input == "ncode":
        x = input("What is your National Code? ")
        information.append(x)
        UserInput.append("fname")
        
    elif Input == "email":
        x = input("What is your Email? ")
        information.append(x)
        UserInput.append("email")
        
    elif Input == "country":
        x = input("What is your Country? ")
        information.append(x)
        UserInput.append("country")
        
    elif Input == "address":
        x = input("What is your address? ")
        information.append(x)
        UserInput.append("address")
        
    elif Input == "extra":
        x = input("add any extra information you want: ")
        information.append(x)
        UserInput.append("extra")
        
    else:
        print("Wrong Input")
        
    if len(UserInput) == 8:
        print("Enough information, lets create your QRCode.")
        break
    
print("Your QRCode is ready.")
User = qrcode.make(information)
User.save("UserInformation.png")

