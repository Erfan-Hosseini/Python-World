def diamond_creator(size, shape):
    price = 0
    for i in range(size):
        print(" " * (size - i - 1) + shape * (2 * i +1))
        price +=300
    
    for i in range (size -2, -1, -1):
        print(" " * (size - i -1) + shape * (2 * i +1))
        price += 300
        
    print("That comes to:", price , "$, thank you for your purchace.")
 
print("Hello and welcome to diamond creator, give me a size and a shape and i will give you a diamond in that size and shape.")
answer = "yes"  

while True:  
    if answer == "yes":
        size = int(input("How big is your diamond? "))
        shape = input("And now what is the material of your diamond? ")
        diamond_creator(size,shape)
        
    print("Do you have another order?")
    answer = input("yes/no: ").lower()
    
    if answer == "yes":
       print("Ok let's create another diamond.")
       
    elif answer == "no":
       print("Let me put your order in a bag, here you go, good luck and have a good day.")
       break
    
    else:
       print("I did'nt hear that, say again?")
    
    
    