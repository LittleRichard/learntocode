# TODO: import the random library
import random

# TODO: prompt user for input number of dice, 1 or 2.
num_dice = input('How many dice? Enter 1 or 2: ')

# TODO: reject the user's input if they give you a value that
# is not 1 or 2 and tell them to scram
if num_dice == '1' or num_dice == '2':
    print('thank you for valid input')
else:
    print('It was so simple, just 1 or 2. SCRAM!')

# Note: that input() always gives you back a string, even if you
# enter an integer value.  Let's clean it up a little.

# EXAMPLE: to convert the input (which python assumes to be a string) 
# into an integer we can use the `int` function...
# assuming that the string is an integer!
user_input_str = '2' # this is the result of input()
# trust but verify: see what happens if you do:
# int('not an integer, obviously')  # should go BOOM
user_input_int = int(user_input_str)
# you can also go the other way with the `str` function
user_input_back_to_str = str(user_input_int)

    
# TODO: prompt user for how many sides those dice should have
num_sides = input('How many sides should the dice have? ')
num_sides = int(num_sides)
num_dice = int(num_dice)

# TODO: roll the number of dice given by the user, print the results
# we'll always roll at least one die
die1 = random.randint(1, num_sides)
if num_dice == 1:
    print(f'you rolled a {die1}')
elif num_dice == 2:
    # only roll the 2nd one if we have to
    die2 = random.randint(1, num_sides)
    print(f'you rolled a {die1} and a {die2}')
else:
    print('Try again!')

# Bonus points if you do some ascii art to make the output
# look like real dice!

