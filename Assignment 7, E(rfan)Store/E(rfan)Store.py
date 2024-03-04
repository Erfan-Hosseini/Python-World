import pyfiglet
import time
import sys
import qrcode

USERS = []
EVERYTHING = []
OWNER = []
cart = []
owner_username = ""
user_username = []
who = ""
n = 0

def show_menu(n=0):
    while True:
        if n == 0:
            """
            customer can see and buy the items. 
            owner can change the inventory(add or remove or edit).
            """
            answer = input("(customer,owner): ").lower()
            if answer == "customer":
                n = 1
                return answer, n
            elif answer == "owner":
                n = 2
                return answer, n
            else:
                print("I dont understand that, try again.\n")
        elif n == 2:
            print("\nOk", owner_username, "what do you want to do now?")
            print("1: Change your name?\n2: Change your password?\n3: See your products?\n4: Edit your products?")
            print("5: Search for a specific item?\n6: Remove a specific product?\n7: Exit.")
            answer = input("Give me the number of your choice: ")
            return answer
        #guest will be added soon
        elif n == 1:
            print("Hello, enter your choice, if you have an account, login and if you don't have it, create one.(Guest option will be added later.)")
            answer = input("(login/create): ")
            n = 3
            return answer,n
        elif n == 3:
            print("\nOk,",user_username[0],"what do you want to do now?")
            print("1: See products?\n2: Search for a specific item?\n3: Add something to your cart?\n4: See your cart?")
            print("5: Buy the filled cart?(it must contain something.)\n6: Change name?\n7: Change password?\n8: Exit.")
            answer = input("Give me the number of your choice: ")
            return answer
        
                
def store_users():
    f = open("Assignment 7/database/customers_information.txt", "r")
    for item in f:
        result = item.split(" ")
        my_dict = {"username": result[0],
                   "password" : result[1].strip()}
        USERS.append(my_dict)
    f.close()
    
def save_changes():
    f = open("Assignment 7/database/EVERYTHING.txt", "w") 
    for item in EVERYTHING:
        line = ",".join([item["code"], item["name"], item["price"], item["count"], item["category"]]) + "\n"
        f.write(line)
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
    with open("Assignment 7/database/owner_information.txt", "r") as f:
        file_content = f.read()
        if file_content == "$":
            OWNER.append(file_content)       
        else:
            result = []
            for item in file_content.split('\n'):
                result.append(item.strip())
            my_dict = {"ownername": result[0],
                       "password" : result[1]}
            OWNER.append(my_dict)


    
def login():
    print("If you have an account, give me the username and password of it, else create an account.")
    username = input("Username: ")
    password = input("Password: ")
    for user in USERS:
        if user["username"] == username and user["password"] == password:
            print("Login was succesful, Hello", username)
            user_username.append(username)
            return
    print("Username or password was incorrect or you don't have an account.")    
                
def create_account():
    print("Let's create an account.")
    check = True   
    while check:
        check = False
        user_username1 = input("Give me your username: ")
        for i in user_username1:
            if i == " ":
                print("Dont use space in your username.\n")
                check = True
                break
                
        for user in USERS:
            if user["username"] == user_username1:
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
            account = user_username1 + " " + password1 + "\n"
            f.write(account)
            f.close
            user_username.append(user_username1)
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
        owner_username = answer
        print("Changes were made",OWNER[0]["ownername"])
               
    else: 
        print("Work in progress, will be added later")
    
def change_password():
    print("Work in progress, will be added later")
    
def owner():
    if OWNER[0] == "$":
        print("Its seems you are the new owner, before we start you must give me a username and password.")
        owner_username = input("Give me your username: ")
        while True:
            password1 = input("Give me a password: ")
            if len(password1) < 8:
                print("The password must be at least 8 digits.\n")
                continue
            password2 = input("Repeat password: ")
            if password1 == password2:
                f = open("Assignment 7/database/owner_information.txt","w")
                f.write(owner_username+"\n")
                f.write(password1)
                f.close
                print("Thank you, changes were made.")
                return owner_username
            else:
                print("Repeated password is diffrent. try again\n")
                
    else:
        owner_username = OWNER[0]["ownername"]
        owner_password = OWNER[0]["password"]
        print("Hello,",owner_username,".")
        m = 3
        n = 3
        while True:
            for chance in range(3):
                answer = input("Enter your Password: ")
                if answer == owner_password:
                    print("password was correct, logged in.")
                    return owner_username
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
    while True:
        answer = input("Name: ").lower()

        matching_items = []
        for item in EVERYTHING:
            if answer in item["name"].lower():
                matching_items.append(item["name"])

        if matching_items:
            print("Matching items:")
            for item in matching_items:
                print(item)
        else:
            print("No matching items found.")
        answer = input("Do you want to search another item?(yes/no): ").lower()
        if answer == "yes":
            print("Ok let's go.")
        elif answer == "no":
            print("Ok.")
            break
        else:
            print("I dont know what that is, so i take that as a no.")
            break
  
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
    print("Welcome to the shopping cart", user_username[0],".")
    cart = []
    while True:
        found1 = True
        found = True
        while found:
            code = input("Enter the code of the item you want to add to the cart: ")
            for item in EVERYTHING:
                if item["code"] == code:
                    found1 = True
                    print(f"Item: {item['name']}")
                    print(f"Count: {item['count']}")
                    print(f"Price: {item['price']}")
                    answer = input("Do you want to add this item?(yes/no): ")
                    if answer == "yes":
                        quantity = int(input("How many do you want? "))
                        if quantity > int(item['count']):
                            print("Sorry, there are not enough items in stock.")
                            found = False
                            break
                        else:
                            item['count'] = int(item['count'])
                            item1 = item["price"].split("$")
                            item1 = int(item1[0])
                            item['count'] = quantity
                            item["price"] = str(item1 * quantity) +"$"
                            item['count'] = str(item['count'])
                            print(f"{quantity} {item['name']} added to your cart.")
                            cart.append(item)
                            found = False
                            break
                    elif answer == "no":
                        print("Ok.")
                        found = False
                        break
                    else:
                        found = False
                        print("Invalid input, i take that as a no.")
                        break
            if not found1:
                print("Item's code not found in the store.")
                break
        choice = input("Do you want to add more items to your cart? (yes/no): ").lower()
        if choice == "yes":
            print("Ok, let's go!")
        elif choice == "no":
            print("Ok.")
            return cart
        else: 
            print("Invalid answer, i take that as a no.\n")
    
def cart_items(cart):
    if len(cart) == 0:
        print("\nYour cart is empty.")
    else:
        print("\nItems in your cart:")
        for item in cart:
            print(f"name: {item['name']}, Quantity: {item['count']}, Price: {item['price']}")


   
    
def buy_items(cart):
    if len(cart) == 0:
        print("\nYour cart is empty.")
    else:
        total_price = 0
        for item in cart:
            item1 = item["price"].split("$")
            total_price = float(item1[0]) + total_price
        print("Total price of your cart is:", total_price,"$")
        confirmation = input("Do you want to proceed with the purchase? (yes/no): ").lower()
        if confirmation == "yes":
            print("Thank you for your purchase!")
            for cart_item in cart:
                for i,store_item in enumerate(EVERYTHING):
                    if store_item["code"] == cart_item["code"]:
                        store_item["count"] = str(int(store_item["count"]) - int(cart_item["count"]))
                        if int(store_item["count"]) < 0:
                            print(f"Error: Not enough stock for {store_item['name']}.")
                            store_item["count"] = "0"
                        EVERYTHING[i]["count"] =store_item["count"]
                        break
                        
            purchase_list = 'E(rfan)Store, Your items: \n'
            for item in cart:
                purchase_list += item["name"]
                if item != cart[-1]:
                    purchase_list += ', '
            
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(purchase_list)
            qr.make(fit=True)
            qr_img = qr.make_image(fill_color="black", back_color="white")
            qr_img.save("purchase_qr.png")
            print("QR code generated for the purchase.")
            cart.clear()
        else:
            print("Purchase canceled.")
    
def exit():
    sys.exit(0)
    

print(pyfiglet.figlet_format("Welcome to \n E (rfan) Store", font="Doom"))
print("----------------------------------------------------------------------------------------------")
time.sleep(1)
print("First off, identify yourself, who are you? ")
who,n = show_menu()
store_items()

if who == "owner":
    store_owner()
    if OWNER[0] == "$":
        owner_username = owner()
    else:
        owner_username = owner()
    while True:
        answer = show_menu(n)
        time.sleep(1)
        if answer == "1":
            change_username(who)
        elif answer == "2":
            change_password()
        elif answer == "3":
            show_items()
        elif answer == "4":
            edit_item()
        elif answer == "5":
            search_item()
        elif answer == "6":
            remove_item()
        elif answer == "7":
            answer = input("Save your changes?(yes/no): ").lower()
            if answer == "yes": 
                save_changes()
                print("Changes saved, Good day boss.")
            elif answer == "no":
                print("Have a good day boss.")
            else:
                print("Wrong answer, still have a good day boss. i dont save your changes.")         
            sys.exit(0)
        else:
            print("Your answer was wrong!")

else:
    store_users()
    answer,n = show_menu(n)
    if answer == "login":
        login()
    while not user_username:
        create_account()
    while True:
        answer = show_menu(n)
        time.sleep(1)
        if answer == "1":
            show_items()
        elif answer == "2":
            search_item()
        elif answer == "3":
           cart = add_to_cart()
        elif answer == "4":
            cart_items(cart)
        elif answer == "5":
            buy_items(cart)
        elif answer == "6":
            change_username(who)
        elif answer == "7":
            change_password()
        elif answer == "8":
            save_changes()
            sys.exit(0)

        else:
            print("Your answer was wrong!")





