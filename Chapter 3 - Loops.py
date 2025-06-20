#Chapter 3: Loops

#Python has two kinds of loops: 'while' and 'for':

    #While:
        # While blocks check a conditional statement repeatedly.
        # Executes over and over as long as the condition is true
        # If you're ever in an infinite loop, ctrl+c will break it in python (keyboard-interrupt)

        # Break statements cause the execution to immediately exit the loop and not check the condition one last time.
        # Continue statements cause the execution to immediately restart the loop and recheck the condition.

# Running this snippet will print 1, 2, 4, and 5 but not 3 because when
# spam is 3, it continues and restarts the loop.
spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        print('Skip!!')
        continue
    print('spam is ' + str(spam))

# Infinite loops can be used to make sure the user interacts in a certain way.
# Here, the program won't progress until the user specifically types 'your name' (no quotes)
# Because the while loop never becomes false otherwise.

name = ''
while name != 'your name':
    print('Please type your name.')
    name = input('>')
print('Thank you!')

# A program that never exits its infinite loop is a very commmon programming bug.
# Here, we modify the previous program to simply break when we get 'your name'.
# It's functionally the same as the above, but uses a break to exit the loop instead.

while True:
    print('Please type your name.')
    name = input('>')
    if name == 'your name':
        break
print('Thank you!')

# Continue statements are used to jump back to the start of the loop and re-evaluate the condition
# (it's worth noting that it's no different from reaching the end of the loop and returning to the beginning.)

# Tip: if your program is trapped in an infinite loop use ctrl-c in the terminal to send a KeyboardInterrupt error
# to crash the program and stop it. Let's improve Mary's password checker from Chapter 2:

while True:
    print('Who are you?')
    name = input('>')
    if name != 'Mary':
        print('I don\'t know you. Try again.')
        continue
    print('Hello, Mary. What\'s the password? (hint: It is a fish.)')
    password = input('>')
    if password == 'swordfish':
        break
    else:
        print("Wrong password!")
print('Access Granted')

# In this iteration of the code, we will continually ask for the name until the user inputs someone we know.
# Then we will ask them for a password and grant access by breaking the loop if they get it right.


# A note on Truthy and Falsey
# Some data types evaluate to True or False and that can behave a bit unexpectedly if you aren't aware of it.
# For instance: a string with characters in it evaluates to "True", but an empty string is "False", the integer
# and floats 0, and 0.0 respectively are False while other values are True.
# To figure out if a value is "Truthy" or "Falsey", just pass it to the "bool" function.

print('int 0 is: ' + str(bool(0))) #False
print('empty string is: ' + str(bool('')))  #False
print('string chris is: ' + str(bool('chris'))) #True
print('5.23: ' + str(bool(5.23))) #True
print('0.00: ' + str(bool(0.00)))  #False
print('-1: ' + str(bool(-1))) #True


# For Loops trigger a specific number of times, as opposed to While loops which are indeterminate.
# in conjunction with the Range function you can be very precise about how many times to run some code
# The range() function can be called with 3 arguments.
# 1st is start, second is end, and third is the step increment.
    #eg: for i in range(0, 10, 2) would count from 0 to 2, going by 2, instead of 1.

#add up all numbers from 0-100, keeping in mind that we're including 100.
total = 0
for num in range(101):
    total = total + num
print("the sum of numbers from 0-100 is: " + str(total))

#You can even supply negative ranges to make range count down:
for i in range(5, -1, -1):
    print("the range index is: " + str(i))

#termination uses the sys.exit function so import that:
import sys

while True:
    print('Type exit to exit.')
    response = input('>')
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
