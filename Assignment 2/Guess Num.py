import random

print("Welcome, Adad haye entekhabi bein che do adadi bashand?(aval adad kochik tar va bad bozorg tar: )")
x = input()
y = input()
tries = 1

RandomNum = random.randint(int(x),int(y))

while True:
    print("Adad hadsi khod ra vared konid")
    UserGuess = input()
    if int(UserGuess) == RandomNum :
        print("Congrats, To bordi")
        break
    elif int(UserGuess) > RandomNum:
        print("Boro payin tar")
        tries = tries + 1
    else:
        print("Boro bala tar")
        tries = tries + 1
print("To ", tries," bar adad vared kardi")
        