#Section 4, lesson 11
# Try and Except statements

#use try/except for catching errors, like dividing by zero
def div42by(divideby):
    try:
        return 42 / divideby
    except ZeroDivisionError:
        print("Error: Division by zero")

print(div42by(2))
print(div42by(12))
print(div42by(0)) ##This line would cause a divide-by-zero error without the try/except
print(div42by(1))

# You can also catch errors without specifying what kind of error -
# this is great for input validation, too
print("How many cats do you have?")
numCats = input()
try:
    if int(numCats) >= 4:
        print("that's a lot of cats")
    else:
        print("That's not too many cats...")
except:
    print('You did not enter a number.')