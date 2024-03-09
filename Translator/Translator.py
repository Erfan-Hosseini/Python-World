import sys
import gtts

def read_file():
    global ep_words   
    with open("Assignment 8/Translator/Translate.txt","r") as f:
        words = f.read().split("\n")
        ep_words = []
        for i in range(0, len(words)-1, 2):
            my_dict = {"en": words[i],"pe":words[i+1]}
            ep_words.append(my_dict)

def en_to_pe():
    answer = input("Enter your English text: ")
    user_sentence = answer.split(" ")
    output = ""

    for sentence in user_sentence:
        for word in ep_words:
            if sentence.lower() == word["en"].lower():
                output = output + word["pe"] + " "
                break
        else:
            output = output + sentence + " "
    print("\n",output)
    print("Do you want to have the voice of english or persian or both aswell? ")
    answer1 = input("english/persian/both/none: ").lower()
    if answer1 == "english":
        voice = gtts.gTTS(answer, lang = "en", slow = False)
        voice.save("Assignment 8/Translator/envoice.mp3")
    elif answer1 == "persian": 
        voice = gtts.gTTS(output, lang = "ar", slow = False)
        voice.save("Assignment 8/Translator/pevoice.mp3")
    elif answer1 == "both": 
        voice = gtts.gTTS(answer, lang = "en", slow = False)
        voice.save("Assignment 8/Translator/envoice.mp3")
        voice = gtts.gTTS(output, lang = "ar", slow = False)
        voice.save("Assignment 8/Translator/pevoice.mp3")
    elif answer1 == "none":
        print("Ok.")
    else:
        print("Wrong input, i take that as none.")
    

def pe_to_en():
    answer = input("Enter your Persian text: ")
    user_sentence = answer.split(" ")
    output = ""

    for sentence in user_sentence:
        for word in ep_words:
            if sentence.lower() == word["pe"].lower():
                output = output + word["en"] + " "
                break
        else:
            output = output + sentence + " "
    print(output)
    print("Do you want to have the voice of english or persian or both aswell? ")
    answer1 = input("english/persian/both/none: ").lower()
    if answer1 == "english":
        voice = gtts.gTTS(output, lang = "en", slow = False)
        voice.save("Assignment 8/Translator/envoice.mp3")
    elif answer1 == "persian": 
        voice = gtts.gTTS(answer, lang = "ar", slow = False)
        voice.save("Assignment 8/Translator/pevoice.mp3")
    elif answer1 == "both": 
        voice = gtts.gTTS(output, lang = "en", slow = False)
        voice.save("Assignment 8/Translator/envoice.mp3")
        voice = gtts.gTTS(answer, lang = "ar", slow = False)
        voice.save("Assignment 8/Translator/pevoice.mp3")
    elif answer1 == "none":
        print("Ok.")
    else:
        print("Wrong input, i take that as none.")
    

def add_words():
    print("\nLet's add a new definition to our list: ")
    en = input("Enter your english word: ")
    pe = input("Enter the definition of that word in persian: ")
    my_dict = {"en" : en , "pe" : pe}
    ep_words.append(my_dict)
    print("Word added, thank you.")
def exit():
    sys.exit(0)

def update_database():
    with open("Assignment 8/Translator/Translate.txt", "w") as f:
        for word in ep_words:
            f.write(word["en"] + "\n")
            f.write(word["pe"] + "\n")

def show_menu():
    print("\n1: English to persian/2: Persian to english/3: Add a word/4: Exit")
    answer = input("What option do you want? ")
    return answer

print("Hello there, i can translate anything to persian and viceversa within my knowledge.")
print("But the grammer is not that good. 8)")
read_file()
while True:
    answer = show_menu()
    if answer == "1":
        en_to_pe()
    elif answer == "2":
        pe_to_en()
    elif answer == "3":
        add_words()
    elif answer == "4":
        update_database()
        print("Have a good day.")
        exit()
    else:
        print("Invalid input, try again.")

