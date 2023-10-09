
import random

for x in range(1,6):
    GuessNum = int(input("Guess a number between 1 to 5:"))
    randomNum =random.Random.randint(random,1,5)

    if GuessNum == randomNum:
        print("Nice, correct guess")
    else:
        print("Sorry, wrong guess")
        print("Random number was:" ,randomNum )