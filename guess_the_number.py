# Guess the number
import random

# cpu will think a random number b/w 1 to 100
cpu = random.randint(1,100)
counter = 5
game = True
while game:
# user is going to guess the number
    guess = int(input("Enter your guess : "))

    # if user has guessed the number correctly
    if cpu == guess:
        print("Congrats, You have guessed the number...")
        game = False
        break
    elif cpu > guess:
        print("You have guessed smaller number...")
    elif cpu < guess:
        print("You have guessed greater number...")
    else:
        print("Invalid Input...")

    counter -= 1
    print("Chances Left :",counter)
    if counter == 0:
        print("You Lose the game...Number was",cpu)
        break

