import random

n = 10

guess_number = int(n * random.random())+ 1
guess = 0
print("GUESSING THE RANDOMLY GENERATED NUMBER")
while guess != guess_number:

    guess = int(input("Enter Number"))
    if guess > 0:
        if guess > guess_number:
            print("Too high...try again")
        elif guess < guess_number:
            print("Too low... try a higher number")
        else:
            print("Ah..giving up so soon?")
            break
    else:
        print("Well done! How did you know?!")
#
