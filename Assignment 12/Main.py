import Media

MOVIES = []

print("Hello and welcome, select one of the options below: ")
Media.Database.store_movies()

while True:
    answer = input("\n1: show information, 2: download, 3: add, 4: remove, 5: search, 6: edit, 7: exit ")

    if answer == "1":
       Media.Media.showinfo()

    elif answer == "2":
        Media.Media.download()

    elif answer == "3":
        Media.Media.add()

    elif answer == "4":
        Media.Media.remove()

    elif answer == "5":
        Media.Media.search()
        

    elif answer == "6":
        Media.Media.edit()
            

    elif answer == "7": 
        print("Have a good day, bye.")
        Media.Database.save_changes()
        break


    else:
        print("Wrong input.")
