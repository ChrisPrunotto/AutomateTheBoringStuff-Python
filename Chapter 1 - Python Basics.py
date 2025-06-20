#Chapter 1
    # Install Python
    # Basic terminology covered.
    # IDLE = Python IDE
    # Interactive Shell is for typing code on the fly, but saving programs lets you reuse
    # Data types:
        # int, floats, strings.
        # ints are whole numbers (e.g. 42)
        # floats are precision decimal (e.g. 42.0)
        # strings hold text (e.g. 'Forty-Two')
    # Values can be stored in variables for later use (e.g. spam = 42)
    # Variables can be used anywhere values can be used (e.g. spam + 1 = 43)

# This program says hello and asks for my name.
    # Execution begins at the top, and flows downward, line by line.
    # print() function displays the value passed to it
    # input() function lets users type in a value, and the optional argument lets you supply a prompt
    # len() functions takes a string value and returns its length
    # int(), str(), and float() functions can be used to convert values from one to another

# Hello World is always a great simple test to make sure a compiler is functional.
print('Hello world')

print('What is your name?') # Ask for their name
my_name = input('> ') #alternatively, I could have used the previous print statement as the prompt instead.
print('It is good to meet you, ' + my_name)
print('The length of your name is ')
print(len(my_name))

print('What is your age?') # Ask for their age
my_age = input('> ')
print('You will be ' + str(int(my_age) + 1) + ' years old in a year.')


# Use type() to determine what type some value or data is:
print(type(42))
print(type(42.0))
print(type('forty two'))
name = 'Zophie'
print(type(name))
print(type(len(name)))

#Rounding and Absolute Values:

print(round(3.14))
print(round(7.7))
print(round(-2.2))

#Argument can be supplied for Decimal places:
print('3.14 rounds to: ' + str(round(3.14, 1)) + ' at 1 decimal place')
print('7.77777 rounds to: ' + str(round(7.77777, 3)) + ' at 3 decimals.')

# Note rounding is done as "bankers" rounding. For numbers that are exactly halfway between two integers (3.5, 5.5,
# 7.5, etc.), the number is rounded to the nearest EVEN integer:

print(round(2.5)) #Rounds to: 2
print(round(3.5)) #Rounds to: 4
print(round(4.5)) #Rounds to: 4
print(round(5.5)) #Rounds to: 6
print(round(6.5)) #Rounds to: 6
print(round(7.5)) #Rounds to: 8
print(round(8.5)) #Rounds to: 8

print(abs(25))
print(abs(-25))
print(abs(-3.14))
print(abs(0))

