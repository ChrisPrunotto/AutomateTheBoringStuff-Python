#Section 8, lesson 19
# Advanced String Syntax

# Simple concat:
spam = 'hello'
eggs = 'world'

print(spam + ' ' + eggs)

#Double quotes:
spam = "This is Alice's cat" #Double quotes allow apostrophies\single quotes in the string.
print(spam)

spam = 'Say hi to Bob\'s mother.' # use escape characters to add single quotes when you need to add a
                                  # character that would otherwise end the line.
print(spam)

# Escape characters list:
# \' = single quote
# \" = double quote
# \t = tab space
# \n = newline (line break)
# \\ = backslash

spam = '\"We\'re testing out the escape character functionality, \" \n\t -- he\\she said'
print(spam)

# Raw strings are the same as normal strings but they begin with a lowercase r.
# Notice the backslash is literally represented.
spam = r'That is carol\'s cat'
print(spam)

# Triple quotes allow you to enter strings across multiple lines, and they'll print that way.
spam = """Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary,
and extortion.
Sincerely,
Bob"""

print(spam)

#Strings are list-like
spam = 'Hello World!'
print(spam[0])      # You can get indexes...
print(spam[2:4])    # ...and slices
print('x' in spam)  # and evaluate whether or not characters appear in them...
print('o' in spam)  # ...like this



# Section 8, lesson 20
# String Methods

# Remember: strings are immutable.
spam = 'Hello World!'
print(spam)
print(spam.upper()) # This displays the uppercase...
print(spam)         #...but didn't actually change it

# You can actually chain method calls, too.
print(spam.upper().isupper())   # This will always return true: spam will be converted to upper case and
                                # then checked if there's uppercase letters in it, returning True.

# Starts/Ends With
spam = 'Hello World!'
print(spam.startswith('H')) #True
print(spam.startswith('W')) #False

# Joining strings
spam = ', '.join(['planes', 'trains', 'automobiles'])
print(spam)

# Splitting strings
spam = 'My name is Chris'.split(' ') # Notice that the spaces aren't kept
print(spam)

spam = 'My name is Chris'.split('s') # Notice how the split character is removed!
print(spam)

# Justifying text
spam = 'Hello'.rjust(10)
print(spam)
spam = 'Hello'.ljust(10)
print(spam)
spam = 'Hello'.rjust(20, '*') # You can also use different fillcharacters
print(spam)
spam = 'Hello'.ljust(20, '-')
print(spam)
spam = 'Hello'.center(20, '=')
print(spam)

spam = 'Hello'.rjust(10)
print(spam)
spam = spam.strip(' ')
print(spam) #strip out spaces - you can also lstrip and rstrip to target the beginning or ending side of the string.

spam = 'SpamSpamSpamBaconSpamEggsSpamSpamSpam'.strip('ampS')    # When you strip, the order of the letters doesn't
                                                                # matter, it'll just strip until it finds the first
                                                                # letter that doesn't get thrown out.
print(spam) # Which is why the middle "Spam" in BaconSpamEggs doesnt' get removed like the rest do.

# Replacement
spam = 'Hello World!'
print(spam.replace('e', 'XYZ'))

#pyperclip copy/paste
import pyperclip
pyperclip.copy('Hello!!!!!') #copies text straight to the clipboard. .paste() is also available.


# Section 8, lesson 21
# String Formatting

#string interpolation
name = 'Alice'
place = 'Main Street'
time = '6 pm'
food = 'turnips'

# This is kind of inconvenient...
print('Hello ' + name + ', you are invited to a party at ' + place + ' at ' + time + '. Please bring ' + food + '.')

# ...String interpolation can aid in readability and is more convenient
print('Hello %s, you are invited to a party at %s at %s. Please bring %s.' % (name, place, time, food))