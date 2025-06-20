# This is a guess the number game.
import random

#establish a random number
secret_number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guesses_taken in range(1, 7):
    guess = int(input('Guess #' + str((guesses_taken)) + ': '))

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        break  # This condition is the correct guess!

if guess == secret_number:
    print('Good job! You got it in ' + str(guesses_taken) + ' guesses!')
else:
    print('Nope. The number was ' + str(secret_number))

# This will print an error if you guess a string, for example, but we'll cover try-except catching later.

#TODO: Add error handling.