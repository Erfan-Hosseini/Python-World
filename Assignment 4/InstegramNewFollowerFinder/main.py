import profile
import instaloader
import getpass

print("Hello and welcome, we want to track how many new followers you get in your Instgram.")

f = open("Assignment 4/InstegramNewFollowerFinder/Follower.txt", "r")
OldFollower = []
for Line in f:
    OldFollower.append(Line)
f.close()

L = instaloader.Instaloader

UserName = getpass.getpass("Enter your Username: ")
Password = getpass.getpass("Enter your Password: ")

L.login(UserName, Password)

print("You got logged in, congrats.")

Profile = instaloader.Profile.from_username(L.context,"Mykweenh")

NewFollower = []

for Follower in Profile.get_followers():
    NewFollower.append(Follower)
    
f = open("Follower.txt", "w")
for Follower in Profile.get_followers():
    f.write(Follower + "\n")
f.close()
 
for NewFollowers in NewFollower:
    if NewFollowers not in OldFollower:
        print(NewFollowers)
        
