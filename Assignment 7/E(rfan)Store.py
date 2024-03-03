import pyfiglet
import time
import sys

USERS = []
EVERYTHING = []
OWNER = []
owner_username = ""
user_username = ""
who = ""

def show_menu(n = 0):
    while True:
        if n == 0:
            """
            customer can see and buy the items. 
            owner can change the inventory(add or remove or edit).
            """
            answer = input("(customer,owner): ").lower()
            if answer == "customer" or answer == "owner":
                n +=1
                return answer,n
            else:
                print("I dont understand that, try again.\n")
                
def store_users():
    f = open("Assignment 7/database/customers_information.txt", "r")
    for item in f:
        result = item.split(" ")
        my_dict = {"username": result[0],
                   "password" : result[1].strip()}
        USERS.append(my_dict)
    f.close()
    
        

def store_items():
    f = open("Assignment 7/database/EVERYTHING.txt", "r")
    for item in f:
        result = item.split(",")
        my_dict = {"code": result[0],
                   "name" : result[1],
                   "price" : result[2],
                   "count" : result[3],
                   "category" : result[4].strip()}
        EVERYTHING.append(my_dict)
    f.close()
 
def store_owner(): 
    f = open("Assignment 7/database/owner_information.txt", "r")
    if f == "$":
        OWNER.append(f)       
    else:
        result = []
        for item in f:
            result.append(item.strip())
        my_dict = {"ownername": result[0],
                   "password" : result[1]}
        OWNER.append(my_dict)
    f.close
    
def login():
    print("If you have an account, give me the username and password of it, else create an account.")
    username = input("Username: ")
    password = input("Password: ")
    for user in USERS:
        if user["username"] == username and user["password"] == password:
            print("Login was succesful, Hello", username)
            return username
    print("Username or password was incorrect or you don't have an account.")    
                
def create_account():
    print("Let's create an account.")
    check = True   
    while check:
        check = False
        user_username = input("Give me your username: ")
        for i in user_username:
            if i == " ":
                print("Dont use space in your username.\n")
                check = True
                break
                
        for user in USERS:
            if user["username"] == user_username:
                print("Username already exist, try another one.\n")
                check = True
                break
                
    check = False
    while True:
        password1 = input("Give me a password: ")
        if len(password1) < 8:
            print("The password must be at least 8 digits.\n")
            continue
        for i in password1:
            if i == " ":
                print("Dont use space in your password.")
                check = True
                break
        if check:
            check = False
            continue
        password2 = input("Repeat password: ")
        if password1 == password2:
            f = open("Assignment 7/database/customers_information.txt","a")
            account = user_username + " " + password1 + "\n"
            f.write(account)
            f.close
            print("Account created.")
            break
        else:
            print("Repeated password is diffrent. try again\n")
                
   
    
    
def change_username(person):
    if person == "owner":
        owner_username = OWNER[0]["ownername"]
        print("Ok", owner_username,"what do you want your new name to be?")
        answer = input("Enter it: ")
        OWNER[0]["ownername"] = answer
        print("Changes were made",OWNER[0]["ownername"])
        
            
        
        
    else: 
        ...
    
def change_password():
    ...
    
def owner():
    f = open("Assignment 7/database/owner_information.txt","r")
    file = f.read()
    f.close
    if file == "$":
        print("Its seems you are the new owner, before we start you must give me a username and password.")
        owner_username = input("Give me your username: ")
        while True:
            password1 = input("Give me a password: ")
            if len(password1) < 8:
                print("The password must be at least 8 digits.\n")
                continue
            password2 = input("Repeat password: ")
            if password1 == password2:
                f = open("Assignment 7/owner_information.txt","w")
                f.write(owner_username+"\n")
                f.write(password1)
                f.close
                print("Thank you, changes were made.")
                break
            else:
                print("Repeated password is diffrent. try again\n")
                
    else:
        f = open("Assignment 7/database/owner_information.txt","r")
        file = f.read().split("\n")
        owner_username = file[0]
        owner_password = file[1]
        f.close
        print("Hello,",owner_username, "\nplease enter your password. ")
        m = 3
        n = 3
        while True:
            for chance in range(3):
                answer = input("Enter your Password: ")
                if answer == owner_password:
                    print("password was correct, logged in.")
                    return "succesful",owner_username
                else:
                    print("Incorrect password, try again. You have", m-1, "tries left.\n")
                    m-=1
            if n == 0:
                print("It seems you have forgotten your password, please contact us for support.")
                sys.exit(0)
            if  m == 0:
                print("Too many incorrect tries.\n")
                for i in range(10,0,-1):
                    print("Wait", i,"seconds.")
                    time.sleep(1)
                m = 3
                print("Careful, you only have", n,"chance left.")
                n-=1       
        
def add_item():
    print("Ok ",owner_username, "let's add some items to the list.")
    print("Give me the item's code, we already have from code 1 to 390, if you did'nt change anything")
    print("give it from 391.\n")
    while True:
       available_code = True
       while available_code:
           code = input("Item's code: ")
           for item in EVERYTHING:
               if item["code"] == code:
                   print("That code", code, "is already in the list.\n")
                   break
           else: 
               available_code = False
               
       print("Code available, now give me the details.\n")
       
       while True:
             answer = input("Categories: (vegetables: 1/groceries: 2/random: 3/furnitures and electronics: 4):  ")
             if answer != "1" and answer !="2" and answer !="3" and answer !="4":
                 print("Invalid category!!\n")                
             else:
                 break
       if answer == "1":
           category = "vegetables"
       if answer == "2":
           category = "groceries"
       if answer == "3":
           category = "random_things"
       if answer == "4":
           category = "furnitures and electronics"
       
       item = []
       item_name = input("Name: ")
       item_price = input("Price: ")
       item_count = input("Count: ")
       item.append(code)
       item.append(item_name)
       item.append(item_price)
       item.append(item_count)  
       item.append[category]
       my_dict = {"code": item[0],
                   "name" : item[1],
                   "price" : item[2],
                   "count" : item[3],
                   "category" : item[4]}
                   
       EVERYTHING.append(my_dict)          
       answer = input("Add another item? (yes/no): ").lower()
       
       if answer == "yes":
           print("Ok let's add another item.")
       elif answer == "no":
           print("Changes were made.")
           break
       else:
           print("Invalid answer, i take that as a no")
           break
       
def remove_item():
    print("Ok let's remove the item you desire.")
    
    while True:
        answer = input("What is the code of your item? ")
        for item in EVERYTHING:
            if item["code"] == answer:
                print("Item found! the item you are looking for is: ", item["name"])
                found_code = answer
                category = item["category"]
                break
        else:
            print("Invalid code, i did'nt find any item with that code.\n")
            continue
        
        print("Do you want to remove that item?")
        answer = input("yes/no: ").lower()
        
        if answer == "yes":
            for i, item in enumerate(EVERYTHING):
                if item["code"] == found_code:
                    EVERYTHING.pop(i)  
                    break
                
            print("Item removed.")
        elif answer == "no":
            print("Time wasted.")
        else:
            print("Invalid answer, i take that as a no.\n")
          
        answer = input("Remove another item?(yes/no): ").lower()
        if answer == "yes":
            print("Ok let's go remove another item.\n")
        elif answer == "no":
            print("Changes were made.\n")
            break
        else:
            print("Invalid answer, i take that as a no.\n")
            break
            
def show_items():
    print("Our store is big, do you want to see everything or specfic category?")
    while True:          
        answer = input("everything/category: ").lower()
        print()
        if answer == "everything":
            for item in EVERYTHING:
                print(item["name"],"| ", end = "")
            print("\n")
            break
            
        elif answer == "category":
            print("We have 4 categories, enter the number of the category you want to see.")
            while True:
                answer = input("Categories: (vegetables: 1/groceries: 2/random: 3/furnitures and electronics: 4):  ")
                while True:
                    if answer != "1" and answer !="2" and answer !="3" and answer !="4":
                         print("Invalid category!!\n")                
                    else:
                         break
                print()
                if answer == "1":
                    for item in EVERYTHING:
                        if item["category"] == "vegetables":
                            print(item["name"],"| ",end = "")
                if answer == "2":   
                    for item in EVERYTHING:
                        if item["category"] == "groceries":
                            print(item["name"],"| ",end = "")
                if answer == "3":
                    for item in EVERYTHING:
                        if item["category"] == "random_things":
                            print(item["name"],"| ",end = "")
                else:
                    for item in EVERYTHING:
                        if item["category"] == "furnitures_and_electronics":
                            print(item["name"],"| ",end = "")
                answer = input("\n\nDo you want to see another category?(yes/no): ").lower()
                if answer == "yes":
                    print("Ok let's go.\n")
                elif answer == "no":
                    print("Ok.\n")
                    break
                else:
                    print("Invalid answer. i take that as a no.\n")
                    break                
        else:
            print("Invalid answer\n")
            continue
        break    
                
    
    
def search_item():
    print("Give me a part of the name of the item you are looking for: ")
    answer = input("Name: ")
    
def edit_item():
    while True:
        answer = input("Give me the code of the item you want to edit: ")
        for i, item in enumerate(EVERYTHING):
            if item["code"] == answer:
                print("Item found! the item you are looking for is: ", item["name"],"\n")
                index = i
                found_code = answer
                break
        else:
            print("Invalid code, i did'nt find any item with that code.\n")
            continue
        answer = input("Do you want to change the details of that item?(yes/no): ")
        if answer == "yes":
            item = [found_code]
            item_name = input("New name: ")
            item_price = input("New price: ")
            item_count = input("New count: ")
            while True: 
                answer = input("Category: (vegetables: 1/groceries: 2/random: 3/furnitures and electronics: 4):  ")
                if answer != "1" and answer !="2" and answer !="3" and answer !="4":
                    print("Invalid category!!\n")                
                else:
                    break
                
            if answer == "1":
                category = "vegetables"
            elif answer == "2":
                category = "groceries"
            elif answer == "3":
                category = "random_things"
            else:
                category = "furnitures_and_electronics"
                
            item.append(item_name)
            item.append(item_price)
            item.append(item_count)  
            item.append(category)
            my_dict = {"code": item[0],
                        "name" : item[1],
                        "price" : item[2],
                        "count" : item[3],
                        "category" : item[4]}
            EVERYTHING[index] = my_dict
            
            
        elif answer == "no":
            print("Time wasted!\n")
        else: 
            print("Invalid answer, i take that as a no.\n")
            
        answer = input("Do you want to edit another item?(yes/no): ").lower()
        if answer == "yes":
            print("Ok, let's go!\n")
        elif answer == "no":
            print("Ok\n")
            break
        else:
            print("Invalid answer, i take that as a no.")
            break
        
         
    
def add_to_cart():
    ...
    
def cart_items():
    ...
    
def buy_items():
    ...
    
def exit():
    ...
    

print(pyfiglet.figlet_format("Welcome to \n E (rfan) Store", font="Doom"))
print("----------------------------------------------------------------------------------------------")
store_items()
store_users()
store_owner()
time.sleep(1)
show_items()
# yadet bashe baraye change username ya change password moghe farakhoni vorodi bedi change_username(who)
print("First off, identify yourself, who are you? ")
who,n = show_menu()
owner()
# age user bood benevis change_username(who)







