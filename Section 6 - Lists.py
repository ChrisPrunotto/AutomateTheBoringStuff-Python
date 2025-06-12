#Section 6, lesson 13
# The List data type

#example list assigned to a variable
spam = ['cat', 'bat', 'rat', 'elephant']

print(spam[0]) #accesses an item based on it's position - these are zero-indexed

#lists can also contain other lists
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam[0]) #will print out the zero index, which is the first list
print(spam[1][4]) #will print out the 4th index in the first index - the number 50

spam = ['cat', 'bat', 'rat', 'elephant']
# Negative values can access items from the end, counting backward - -1 being the last index
print(spam[-1]) #elephant
print(spam[-2]) #rat

# Slices of a list can get multiple items in a range
print(spam[1:3]) #bat, rat - note that the slice goes up to but does not include the second index


# List replacement, etc.
spam = [10, 20, 30, 40, 50]
print(spam)
spam[1] = 'hello' #replaces a value at a certain index with a new value
print(spam)

print(spam[1:]) #by not indicating the end, you just slice to the end of the list.
print(spam[:3]) #by not indicating the beginning, you just slice from the start of the list.

del spam[1] #delete an index
print(spam)

list1 = [1,2,3]
list2 = [4,5,6]

#lists can also be concatenated
print(list1 + list2)

#converting a string to a list
print(list('Hello'))


# Evaluating if something is in a list:
print('howdy' in ['hello', 'hi', 'howdy', 'heya'])
print('howdy' not in ['hello', 'hi', 'howdy', 'heya'])
print('hey' not in ['hello', 'hi', 'howdy', 'heya'])


# Section 6, lesson 14
# For Loops w/Lists, Multi-assignment and augmented operators

#Lesson 6, we saw ranges and we're revisiting them.
# Ranges are "list-like" objects. range(4) or range(0,4) are represented, sort of, as lists
# that would resolve as [0,1,2,3] - these are technically sequences, but here they operate like lists.

#these are basically equivalent
for i in range(0, 4):
    print(i)

for i in [0, 1, 2, 3]:
    print(i)

#we can print out what the actual values of the range are by passing it to the list function:
print(list(range(4)))

#count to 50 by 2s, combining the above with the 'step' argument.
print(list(range(0, 100, 2)))

# Example use case of a for loop using a list
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# You can also multi-assign. Take this example, where we set attributes based on a list one at a time...
cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

#...Or we can do it all at once, going through the list one by one. First value gets assigned  to the first variable,
# second value gets assigned to the second variable, and so on.
size, color, disposition = cat

print(size)
print(color)
print(disposition)

# You can also do it by just explicitly indicating in a single line, without a list.
size, color, disposition = 'skinny', 'black', 'quiet'

print(size)
print(color)
print(disposition)

# Swap operations are also simple in this way:
a = "AAA"
b = "BBB"
print("A: " + a)
print("B: " + b)

# to Swap, you can this:
a, b = b, a
print("A: " + a)
print("B: " + b)

#augmented operators, mostly just shortcuts:
spam = 42
print(spam)
#increment the long way
spam = spam + 1
print(spam)

#increment shortcut:
spam += 1
print(spam)
#decrement shortcut
spam -= 1
print(spam)

spam *= 2
print(spam)

spam /= 3
print(spam)

spam %= 4
print(spam)


# Section 6, lesson 15
# Methods

spam = ['hello', 'hi', 'howdy', 'heya']
print('Index \'hi\' found at: ' + str(spam.index('hi'))) #finds the index containing 'hi', or index 1

#error if you don't find something in the list
try:
    spam.index('qeojgktqg')
except ValueError:
    print('Value not found in list')


spam = ['Zoe', 'Bob', 'Fig', 'Bob']
print('Bob found at index: ' + str(spam.index('Bob'))) #only the first one is returned
print(spam)
spam.remove('Bob') #Only the first instance of bob is deleted
print(spam)

del spam[0] #Remove a specific index, in this case Zoe
print(spam)

#append adds to the end
spam.append('Ronnie')
print(spam)

#insert can add anywhere in a list, at the given index
spam.insert(2, 'Binx')
print(spam)

#append and insert are methods that only belong to list types. You can't "append" or "insert" to strings, for example
eggs = 'Hello'
try:
    eggs.append('World')
except AttributeError:
    print('No method append for string data type')

#Lists with numbers can be sorted
spam = [2, 5, 3.15, 1, -4]
spam.sort() #sort in order
print(spam)
spam.sort(reverse=True) #Or reverse-sort!
print(spam)

#works with strings too!
spam = ['ant', 'dog', 'badger', 'piggy']
spam.sort()
print(spam)

#You can't sort lists with mixed ints/strings though
spam = ['ant', 'dog', 'badger', 'piggy', 4.1, 52, 7]
try:
    spam.sort()
except TypeError:
    print('Can\'t sort lists with mixed types.')

#Something to note: Sorting is not in alphabetical order, it's in "asciibetical order' so caps come before lowercase
spam = ['Alice', 'Bob', 'charles', 'Dana', 'amy', 'Chris']
spam.sort()
print(spam)

#to sort in true alphabetical order, try the string.lower key:
spam.sort(key=str.lower)
print(spam)

# Section 6, lesson 16
# Similarities between Lists and Strings

#many things you can do with strings, you can do with lists
list('Hello')
name = 'Chris'
print(name[0])

#...But there's some important distinctions. For one: Lists are mutable, strings are immutable
name = 'Zophie the cat'
print(name[7]) #retrieve the 7th index...
try:
    name[7] = 'X' #attempt to replace the 7th index with something else...
except TypeError:
    print('Can\t assign a value to string objects')

#if you want to change/modify a string, create a new one using slices
name = 'Zophie a cat'
print(name)
newName = name[0:7] + 'the' + name[8:12]
print(newName)

#importantly, lists are referenced.
spam = [0, 1, 2, 3, 4, 5] #this list is a reference to a list in memory.
cheese = spam
cheese[1] = 'Hello!' #change index 1 in the list, but it's a reference so, even when we change it only in 'cheese'...
print(cheese)
print(spam) #...spam also gets changed, too. Be careful about this!

#ANY mutable value uses this referencing system. Immutable values don't have this problem.


#References also have another knock-on effect...modifying parameters in the local scope winds up affecting them globally
def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam) #here, because the list is referenced in memory, "Hello" is appended...

#but for strings, that are immutable...
def eggy(someParameter):
    someParameter += ' World'
    print('local scope: ' + someParameter)

spam = 'Hello'
eggy(spam)
print('global scope: ' + spam) #see how the changes don't pass back to the global variable this time?

# As for the "why", it's because lists can be really large in size, imagine a list that's billions of indexes in size.
# So handling it as a reference keeps memory down, so we don't have to copy them repeatedly.

# If we want to actually copy the list though, you can.
import copy
spam = ['A', 'B', 'C', 'D', 'E', 'F']
cheese = copy.deepcopy(spam) #create a whole copy
print("spam: " + str(spam))
cheese[1] = 42 #now we can edit the new list
print("cheese: " + str(cheese)) #and printing them proves they're not referencing the same location in memory

#White space is normally very important but there are situations where python will ignore indentations:
#...like creating a list
spam = ['apples',
        'oranges',
        'bananas'
        'cats']

#...or strings, using the \ continuation character
print('Four score and seven ' + \
      'years ago')

print(50 + \
      50)