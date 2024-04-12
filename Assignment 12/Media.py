import pytube


MOVIES = []

class Database:
    def __init__(self) -> None:
        pass

    def store_movies():
        f = open("Assignment 12/Media.txt", "r")
        for item in f:
            result = item.split("@")
            movie = Media(result[0],
                    result[1],
                    result[2],
                    result[3],
                    result[4],
                    result[5].strip())
            MOVIES.append(movie)
        f.close()
    def save_changes():
        f = open("Assignment 12/Media.txt", "w") 
        for item in MOVIES:
            line = "@".join([item.name, item.diractor, item.imdb, item.url, item.duration,item.casts]) + "\n"
            f.write(line)
        f.close()      
 


class Media:
    def __init__(self,name,diractor,imdb,url,duration,casts):
        self.name = name
        self.diractor = diractor
        self.imdb = imdb
        self.url = url
        self.duration = duration
        self.casts = casts

    @staticmethod
    def showinfo():
        print("For now, we only have 10 movies, enter a number between 1 and 10 to see their details.")
        answer = input("Only number from 1 to 10: ")
        if 1 <= int(answer) <=10:
            movie = MOVIES[int(answer)-1]
            print("Movie name: ",movie.name,"\n",movie.diractor,"\n",movie.imdb,"\n",movie.duration,"Minutes","\n", movie.casts)
        else:
             print("Your answer was not between 1 and 10")

        
    @staticmethod
    def download():
        print("Do you want to download from Youtube or from the list of our movies?")
        answer = input("youtube/list: ")
        if answer == "youtube":
            print("give me the exact URL you want to download from youtube.")
            answer = input()
            movie = pytube.YouTube(answer).streams.first()
            movie.download(output_path="Assignment 12", filename="youtube.mp4")
        elif answer == "list":
                print("Give me a part of the movie from our list you want to download.")
                answer = input()
                for item in MOVIES:
                    if answer in item.name:
                        print("Do you want to download the movie", item.name,"?")
                        answer = input("yes/no: ").lower()
                        if answer == "yes":
                            movie = pytube.YouTube(item.url).streams.first()
                            movie.download(output_path="Assignment 12", filename="movie.mp4")
                            break
                        elif answer == "no":
                            print("Ok, if that was not your movie, try to be more specefic.")
                            break
                        else:
                            print("Wrong input.")
                            break
    @staticmethod
    def add():
        movie = []
        name = input("Enter the name of the movie: ")
        diractor = input("Enter the name of the diractor for the movie: ")
        imdb = input("Enter the IMDB score of the movie: ")
        url = input("Enter the url of the movie in Youtube: ")
        duration = input("Enter the duration of the movie: ")
        cast = input("Enter the name of the casts for the movie: ")
        movie = Media(name,diractor,imdb,url,duration,cast)
        MOVIES.append(movie)
        print("Movie added.")

    @staticmethod
    def search():
        print("Give me a part of the movie you want to see from the list.")
        answer = input()
        for item in MOVIES:
            if answer in item.name:
                print("Found movie: ", item.name)
            else:
                continue
        
    @staticmethod
    def remove():
        print("Give me a part of the movie you want to remove from the list.")
        answer = input()
        for i, item in enumerate(MOVIES):
            if answer in item.name:
                print("Do you want to remove the movie named", item.name,"?")
                answer = input("yes/no: ").lower()
                if answer == "yes":
                    MOVIES.pop(i)  
                    print("Movie, removed.")
                    break
                elif answer == "no":
                    print("Ok")
                else:
                    print("Wrong input.")

    @staticmethod
    def edit():
        print("Give me a part of the movie you want to edit.")
        answer = input().lower()
        for item in MOVIES:
            print("Checking movie:", item.name)
            if answer in item.name.lower():
                print("Found a matching movie:", item.name)
                print("Do you want to edit the movie named", item.name, "?")
                answer = input("yes/no: ").lower()
                if answer == "yes":
                    new_name = input("Give me a new name for the Movie: ")
                    new_diractor = input("Give me a new diractor: ")
                    new_imdb = input("What is the imdb score? ")
                    new_url = input("What is the youtube URL? ")
                    new_duration = input("What is the duration for the movie? ")
                    new_casts = input("Give me the casts for the movie: ")
                    new_obj = Media(new_name,new_diractor,new_imdb,new_url,new_duration,new_casts)
                    MOVIES.append(new_obj)
                    break
                elif answer == "no":
                    print("Ok")
                else:
                    print("Wrong input.")


             
             
                    

class Movies(Media):
        def __init__(self,box_office,year):
             super().__init__()
             self.box_office = box_office
             self.year = year

class Series(Media):
        def __init__(self,episodes,seasons):
            super().__init__()
            self.episodes = episodes
            self.seasons = seasons
          
class Documentary(Media):
    def __init__(self,location,voice_actor):
            super().__init__()
            self.location = location
            self.voice_actor = voice_actor

class Clip(Media):
     def __init__(self):
          super().__init__()

class Actor(Media):
     def __init__(self,casts):
          super().__init__(casts)

Database.store_movies()






