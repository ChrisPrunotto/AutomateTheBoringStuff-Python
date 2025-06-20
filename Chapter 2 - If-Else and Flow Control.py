#Chapter 2, If Else, and Flow Control
#Types investigated:

# Bools: True, or False - note capitilzation

# Comparison Operators: ==, !=, <, >, <=, >=
# Note that double == is comparison, single = is assignment

#Boolean Operators are and, or, and not (again, note capitalization)

#Quick examples:
print(42 == 42) #True
print(42 == "Hello") #False
print(42 == 41) #False
print(2 != 3) #True
print(42>100) #False
print(42<100) #True
print(True and True) #True
print(True or False) #True
print(False and True) #False
print(False or False) #False
print (not False) #True

# You can even mix booleans and comparison operations:
print( (4 < 5) and (5 < 6)) #True
print( (4 < 5) and (9 < 6)) #False
print( (1 == 2) or (2 == 2)) #True

# Chapter notes:
    # -- Reviewed basic operators and comparisons
    # -- review "Truth Tables" for expression logic.
    # -- Refreshing memory on types

# Components of Flow Controls:
    # Flow Control statements start with a condition and are always followed by a clause.
    # Booleans such as the above are one type of condition.

username = "Mary" # Change "Mary" to print second 'else' statement
password = 'swordfish'
if username == 'Mary':
    print('Hello, Mary')
    if password == 'swordfish':
        print('Access granted')
    else:
        print('Access denied')
else:
    print('Who are you?')


# Elif's are a way of checking for multiple possible conditions. Note that the first true one will run, the rest won't
# be evaluated at all.

name = 'Carol' #Change name to 'Alice' for the "Hi, Alice" greeting, or...
age = 3000 #Change age to get a different response.
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')

# the most basic function blocks are defined with sytax 'def functionName():'
# indentation IS meaningful and defines there the function ends.

# Note that defining a function does not run it. None of this would run just by being part of the file:
def displayIntro():
    print('You approach two spooky caves...') #indentation level 1
    print('which one will you go into?')
    print()

#indentation resets and we can declare a new block of code
def chooseCave():
    cave = ''
    while cave != '1' and cave != '2': # Notice we move to indentation level 2 here:
        print('Which cave while you go into? (1 or 2)')
        cave = input('> ')

    if cave == '1':
        print ("eaten. :(")
    if cave == '2':
        print ("congrats!")


    return cave

#Here, we can two functions we defined
displayIntro()
chooseCave()
