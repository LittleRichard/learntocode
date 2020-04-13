# TODO: import the random library


# TODO: prompt user for input number of dice, 1 or 2.

# TODO: reject the user's input if they give you a value that
# is not 1 or 2 and tell them to scram

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

# TODO: roll the number of dice given by the user, print the results

# Bonus points if you do some ascii art to make the output
# look like real dice!

