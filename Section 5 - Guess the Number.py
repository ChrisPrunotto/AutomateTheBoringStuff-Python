#Section 5, lesson 12
# Writing a "Guess the Number" program

import random

print('Hello, what is your name?')
name = input()

print('Well, ' + name + ' I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break #if it's not too high, and not too low, then it's correct

if guess == secretNumber:
    print('Good job, you guessed my number! It took you ' + str(guessesTaken) + ' guesses.')
else:
    print('Sorry, the number I was thinkg of was ' + str(secretNumber))
