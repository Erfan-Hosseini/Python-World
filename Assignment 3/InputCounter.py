print("Hello and welcome to InputCounter, please give me a sentence and i will count how many words are used in there")

Sentence = input("Enter a sentence: ")
WordCount = 0
Word = False

for i in Sentence:   
    if i == " ":
        if Word:
            WordCount += 1
            Word = False
    else:
        Word = True

if Word:
    WordCount += 1

print("Number of words in your sentence:", WordCount)
