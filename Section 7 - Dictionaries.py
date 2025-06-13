#Section 7, lesson 17
# The Dictionary data type

#Dictionaries are like lists but can use many types
#They have keys and are associated with value as key-value pairs.

#syntax: dictionary = {key1 : value1, key2 : value2, ...}
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

print('My cat has ' + myCat['color'] + ' fur.')

#to note, dictionaries are unordered, despite the implication in the name. The following can't sort.
spam = {12345: 'Luggage combination', 42: 'The answer'}

#Because these aren't ordered, these are the same:
eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
ham = {'species': 'cat', 'age': 8, 'name': 'Zophie'}

#Returns true
print(eggs == ham)

#You can search for if a key exists
print('name' in eggs)

#You can return list-like objects of keys, values, or items:
print(list(eggs.keys()))
print(list(eggs.values()))
print(list(eggs.items())) #this last one returns two-item tuples.


#These are not lists though!

for k in eggs.keys():
    print(k)

for v in eggs.values():
    print(v)

for i in eggs.items():
    print(i)

for k, v in eggs.items():
    print(str(k) + ": " + str(v))

# Trying to access a key that doesn't exist will crash a program, so Python offers a "get"
# method to safely try and return it, with an optional fallback value
print(eggs.get('age'))

print(eggs.get('favorite food', 'not found'))

picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('napkins', 0)) + ' napkins to the picnic.')

#you can set a value like this
if 'color' not in eggs:
    eggs['color'] = 'black'

# Or use the default-setter to only set it if it doesn't exist.
# It's a shortcut to only set the value if it doesn't already exist
print(eggs)
eggs.setdefault('weight', '3lb')
print(eggs)
eggs.setdefault('weight', '9lb')
print(eggs)


# Counting occurrences in a string

message = 'It was a bright cold day in April, and the clocks were striking thirteen'
count = {} #storing each letter and it's occurance count

for character in message.upper():
    count.setdefault(character, 0)  # We need to set the default for every character
                                    # to make sure it's added and set to zero before we increment...
    count[character] += 1           # otherwise, this line fails by trying to increment a nonexistent key-value pair.

print(count)

#if we wanted to, we could then "pretty-print" this like this:
import pprint

pprint.pprint(count) #creates this in a neater columm format.

#or we can format it as a string (which prints to the console identically, but can be used as a string)
charcounttext = pprint.pformat(count)
print(charcounttext)

# Section 7, lesson 18
# Data Structures

cat = {'name': 'Zophie', 'age': 7, 'color': 'grey'}
allCats = []
allCats.append({'name': 'Gips', 'age': 13, 'color': 'tabby'})
allCats.append({'name': 'Binx', 'age': 8, 'color': 'grey'})
allCats.append({'name': 'Grey', 'age': 10, 'color': 'grey/white'})
print(allCats)


## Data structures can represent collections of data - here's an example of a tic-tac-toe board
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

pprint.pprint(theBoard)

theBoard['mid-M'] = 'X'
pprint.pprint(theBoard)

theBoard['top-L'] = 'X'
theBoard['top-M'] = 'O'
theBoard['top-R'] = 'X'
pprint.pprint(theBoard)

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-M'] + '|' + board['mid-R'] + '|' + board['mid-L'])
    print('-----')
    print(board['low-M'] + '|' + board['low-R'] + '|' + board['low-L'])

printBoard(theBoard)

## Obviously, we'll need more than just this to make such a game functional, but importantly, the data structure
## allows us everything we need to represent the state of the game!