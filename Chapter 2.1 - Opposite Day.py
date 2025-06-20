#Chapter 2, lesson 6

#Asking the important question: is today opposite day?

today_is_opposite_day = True

# Answer honestly, if today is opposite day, we'll say it's opposite day:
if today_is_opposite_day == True:
    say_it_is_opposite_day = True
else:
    say_it_is_opposite_day = False


#and if it is opposite day, we have to say it's not:
if today_is_opposite_day == True:
    say_it_is_opposite_day = not say_it_is_opposite_day

#And then we say what day it is:
if say_it_is_opposite_day == True:
    print('Today is opposite day')
else:
    print('Today is not opposite day')


# Logically, no matter what you set "today_is_opposite_day" to, True or False, we'll always print
# that today is NOT opposite day, because we flip the bool to False if it is.