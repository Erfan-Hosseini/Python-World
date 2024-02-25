import random

print("Hello and welcome to Hangman, do you want to start or do you want to see the list of names or add/remove your own words? ")

Names = ["broom","mop","bucket","sponge","detergent","brush","vacuum","dustpan","trashcan","recycling","plant","flower",
    "tree","shovel","rake","wheelbarrow","hose","sprinkler","seeds","lawnmower","fertilizer","wheel","hammer","screwdriver",
    "wrench","pliers","nails","screws","tape","measure","level","drill","saw","ladder","paintbrush","roller","paint","can",
    "sandpaper","caulk","putty","glue","gun","duct","tape","pliers","box","cutter","tarp","extension","cord","bolt","nut","washer",
    "twine","wire","rope","string","stapler","staples","push","pins","thumbtacks","safety","pins","sewing","needle","thread","fabric",
    "yarn","buttons","zipper","hook","eye","velcro","ribbon","lace","elastic","bias","snap","pin",
    "zip","tie","buckle","braid","grommet","buttonhole","fastener","seam","ripper","iron","ironing","board","sewing","machine","serger",
    "knitting","needles","crochet","pattern","gauge","measuring","chalk","yardstick","meterstick","weights",
    "pincushion","dress","form","marker","scissors","rotary","cutting","mat","thimble","embroidery","hoop","needle","threader",
    "french","curve","maker"]



while True:
    Answer = input("start/see/add/remove/exit: ")
    Answer = Answer.lower()
    
    if Answer == "start":
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        RightChar = []
        WrongChar = []
        n = 0
        Word = random.choice(Names)
        print("How difficult do you want the game to be?")
        Difficulty = input("easy/normal/hard/impossible: ")
        Difficulty = Difficulty.lower()
        
        if(Difficulty == "easy"):
            Chances = 100
        elif(Difficulty == "normal"):
            Chances = 6
        elif(Difficulty == "hard"):
            Chances = 3
        elif(Difficulty == "impossible"):
            Chances = 1
        else:
            print("There is a typo in your input, so you wanted impossible, huh?")
            Chances = 1
        
        while n<Chances:
            
            print(Chances, "Chance Remain")
            for i in range(len(Word)):
                if Word[i] in RightChar:
                    print(Word[i], end="")
                else:
                    print("_ ",end="")
            if len(RightChar) == len(Word)-1:
                print(" ,Congrats, You guessed the word")
                break

            UserGuess = input("  Guess the Alphabet: ")
            UserGuess = UserGuess.lower()
            if len(UserGuess) != 1:
                print("Enter only one letter smart ass")
            elif UserGuess not in alphabet:
                print("You have already guessed that alphabet")
            elif UserGuess in Word:
                print("Well done, there is a/an",UserGuess,"in the word")
                RightChar.append(UserGuess)
                alphabet.remove(UserGuess)
            else:
                print("There is no",UserGuess,"in the word")
                WrongChar.append(UserGuess)
                alphabet.remove(UserGuess)
                Chances = Chances -1
            if Chances == 0:
                print("Sorry, you lost, the word was: ",Word)
    elif Answer == ("see"):
        print("Ok, lets see the words: ")
        print(Names)
    elif Answer == ("add"):
        print("Enter the word you want to add: ")
        add = input()
        Names.append(add)
        print("Name added")
    elif Answer == ("remove"):
        print(Names)
        print("What name do you want to remove? ")
        remove = input()
        if remove in Names:
            Names.remove(remove)
            print("Name removed")
        else:
            print("Invalid input")
    elif Answer == "exit":
        print("Good luck")
        break
    else:
        print("I think there is a typo in your input, try again")
        
        
            
        

