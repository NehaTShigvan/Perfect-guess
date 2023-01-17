import random

randNum = random.randint(1, 100)
print(randNum)
userGuess = None
guesses = 0
while(userGuess != randNum):
    userGuess = int(input("Guess a number between 1-100: "))
    guesses += 1
    if userGuess == randNum:
        print("Bingo! You guessed the correct number!")

    else:
        if userGuess > randNum:
            print("You guessed it wrong. Guess the smaller number.")
        else:
            print("You guessed it wrong. Guess the larger number.")

print(f"You guessed the number in {guesses} guesses.")
