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
        print("Give me a part of the movie you want to edit.")
        answer = input()
        for i, item in enumerate(MOVIES):
            if answer in item[0]:
                print("Do you want to edit the movie named", item[0],"?")
                answer = input("yes/no: ").lower()
                if answer == "yes":
                    Media.MOVIES[i].edit()
                    MOVIES.pop(i)  
                    break
                elif answer == "no":
                    print("Ok")
                else:
                    print("Wrong input.")
            

    elif answer == "7": 
        print("Have a good day, bye.")
        Media.Database.save_changes()
        break


    else:
        print("Wrong input.")