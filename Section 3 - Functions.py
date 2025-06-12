#Section 3, lesson 8
# Exploring python's built in functions

import random
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))

# import random, sys, os, math etc.
from random import *

# once you've imported a module, you don't have to follow the module.function() nomenclature,
# but be aware that this affects readability.
print(randint(1,10))

# modules can be imported to gain access to new functions
# Modules that come with Python are the "Standard" library.
# You can also install third-party modules using the pip tool. One such example is pyperclip,
# which will be used in this course.

# installing pyperclip using the cmd prompt!


#Section 3, lesson 9
# Writing our own functions

def hello():
    print('howdy!')
    print('Howdy!!')
    print("howdy-doodie buckaroonie")

#by doing this, you can repeatedly run frequently-run code
hello()
hello()
hello()

# Principle: DRY ("don't repeat yourself")

#Arguments that can be passed to functions
def helloThere(name):
    print('Hello ' + name + ".")

helloThere("Alice")
helloThere("Bob")


def plusOne(number):
    return number + 1

newNumer = plusOne(5)
print(newNumer)

#To keep in mind: print() returns the None type.
# Example

spam = print()
print(spam == None) #should return True

#Optional argument example for print:
print('Hello', end='') #avoid newline by changing the endchar to '' isntead of the default \n
print('World') #creating 1 line of text between the two.
print('cat', 'dog', 'mouse', sep="___")


#Section 3, lesson 10
# Local and Global scope

spam = 42 #Global variable/scope

def eggs():
    spam = 42 # local variable/scope (ie: within a function, this won't
              # exist once the function is no longer needed)

# Global scope iscode outside of all functions.
# Functions have their own local scope. Values assigned within them are local.

#example of nonfunctional code:

# def spam():
#     eggs = 99
#
# spam()
# print(eggs)

# local scope functions also can't use the scope of another local function's local variable

def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()  #this should print 99, because the local scope of eggs in spam
        # isn't the same as the 'eggs' in bacon.

def spam2():
    eggs = 'Hello'
    print(eggs)

eggs = 42
spam2()
print(eggs) # This should print "hello" and then 42.
            # The first print is from the spam2 function where "hello" get assigned
            # to eggs and then printed, and returning the main flow, eggs is printed
            # but there's no usage of the "Hello" string since that's a local variable.