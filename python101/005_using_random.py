import random # import is how you tell python that you want to use a library in a script

# python convention: ALL_CAPS to indicate that a variable is a 'constant' that is easy to change
# in one place to alter the behavior of the script, but is NOT a variable that should
# be overwritten by other stuff when executing the script.
# NOTE: the ALL_CAPS will be important later when we discuss 'scope', but for
# now just trust me.
MAX_VALUE = 250

# this is calling the 'randint' function in the 'random' library
my_rand_int = random.randint(1, MAX_VALUE) # between the 1st argument and the 2nd, inclusive
print(my_rand_int)

# the random library can do lots of other things, but involve data types
# and data structures that we'll get to soon.

print('') # print a blank line

# confirm by:
## grab a random integer between 0 and 50
my_rand_int = random.randint(0, 50) # between the 1st argument and the 2nd, inclusive
# simulate rolling 2 dice, what's the resulting sum?
dice_total = random.randint(1, 6) + random.randint(1, 6)
## print the result
print(dice_total)