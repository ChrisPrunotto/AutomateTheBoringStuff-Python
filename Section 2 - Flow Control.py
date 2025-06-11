#Section 2, lesson 4
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

# Section notes:
    # -- Reviewed basic operators and comparisons
    # -- review "Truth Tables" for expression logic.
    # -- Refreshing memory on types

#Section 2, lesson 5, code excerpt
    # -- function blocks are defined with def,
    #    semicolon, and indentation (NOT curly braces!)

def displayIntro():
    print('You approach two spooky caves...')
    print('which one will you go into?')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave while you go into? (1 or 2)')
        cave = input()

    if cave == '1':
        print ("eaten. :(")
    if cave == '2':
        print ("congrats!")


    return cave

displayIntro()
chooseCave()

#Section 2, lesson 6, while loops code excerpts:
    # While blocks check a conditional statement repeatedly.
    # If you're ever in an infinite loop, ctrl+c will break it in python (keyboard-interrupt)

    # Break statements cause the execution to immediately the loop and not check the condition one last time.
    # continue statements cause the execetion to immediately restart the loop and recheck the condition.

# Running this snippet will print 1, 2, 4, and 5 but
# not 3 because when spam is 3, it continues and restarts the loop.
spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        print('Skip!!')
        continue
    print('spam is ' + str(spam))

# Section 2, lesson 6, for loops
# For Loops trigger a specific number of times. The range() function can be called with 3 arguments.
# 1st is start, second is end, and third is the step increment.
    #eg: for i in range(0, 10, 2) would count from 0 to 2, going by 2, instead of 1.

#add up all numbers from 0-100, keeping in mind that we're including 100.
total = 0
for num in range(101):
    total = total + num
print("the sum of numbers from 0-100 is: " + str(total))

