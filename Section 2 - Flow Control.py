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

    if cave == '2':
        print ("congrats!")

    return cave

displayIntro()
chooseCave()