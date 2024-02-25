print("Welcome to the Fibonacci sequence, until how many sequence do you want to see?")
until = input("Enter a number: ")
n = 0
sequence = 1
sequence1 = 0
sum=0
print(sequence1)
print(sequence)
while n < int(until):
    sum = sequence1 + sequence
    sequence1 = sequence
    print(sum)
    sequence = sum
    n = n + 1
while True:
    Answer = input("Do you want to know the next sequence?(yes/no) ")
    if Answer == "yes":
        sum = sequence1 + sequence
        sequence1 = sequence
        print(sum)
        sequence = sum
    elif Answer == "no":
        print("Until later")
        break
    else:
        print("Invalid answer, try again(yes/no)")
