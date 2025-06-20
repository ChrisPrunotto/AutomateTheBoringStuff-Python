# Pattern Matching and RegEx

# RegEx is kind of like a mini language just for matching text patterns.
# Take the Phone number. You can sort of expect that it's 3 digits, a dash, 3 more digits, a dash, and four numbers.

# By identifying patterns you can immediately tell that...
# 555-666-5555 is a phone number.
# 5556665555 is not
# despite the fact that they're both "the same number"

# Recognizing simple patterns can be very difficult. For example, here's a simple
# attempt at checking if something's a phone number:

def isPhoneNumber(text):
    if len(text) != 12:
        return False #it's not phone number sized
    for i in range(0-3):
        if not text[i].isdecimal():
            return False #no area code
    if text[3] != '-':
        return False #no dash separator
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False #no first-3-digits
    if text[7] != '-':
        return False #no second dash separator
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False #missing last 4 digits
    return True

print(isPhoneNumber('555-666-5555'))

# This is a lot of code, and it's severely limited because it can't check within a wider string of text.
# If you wanted to do that....
message = 'Call me at 415-555-1101 tomorrow, or at 555-666-5555 for this great deal!'
foundNumber = False

for i in range(len(message)):
    chunk = message[i:i+12] #grab a 12-character chunk of text using a slice of the message
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('No phone number found!')

# Regex can simplify all of this into just a few lines:
import re #regex module

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')   # use raw strings to make sure we don't have
                                                        # to escape characters! \d is the key for a digit
mo = phoneNumRegex.search(message) #mo = "match object"

print('Found phone number with RegEx: ' + mo.group())


phoneNumRegex.findall(message) #FindAll will return a list of all matching objects, not just the first.
print('Found phone number(s): ' + str(phoneNumRegex.findall(message)))