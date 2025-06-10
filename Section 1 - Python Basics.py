#Section 1, lesson 1
    # Install Python

#Section 1, lesson 2
    # Basic terminology
    # IDLE = Python IDE
    # Interactive Shell is for typing code on the fly, but saving programs lets you reuse
    # Data types:
        # int, floats, strings.
        # ints are whole numbers (e.g. 42)
        # floats are precision decimal (e.g. 42.0)
        # strings hold text (e.g. 'Forty-Two')
    # Values can be stored in variables for later use (e.g. spam = 42)
    # Variables can be used anywhere values can be used (e.g. spam + 1 = 43)


#Section 1, lesson 3
# This program says hello and asks for my name.
    # Execution begins at the top, and flows downward, line by line.
    # print() function displays the value passed to it
    # input() function lets users type in a value
    # len() functions takes a string value and returns its length
    # int(), str(), and float() functions can be used to convert values from one to another

print('Hello world')

print('What is your name?') # Ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is ')
print(len(myName))

print('What is your age?') # Ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' years old in a year.')

# Section notes:
# -- Installing Py
# -- Debugging
# -- Refreshing memory on types