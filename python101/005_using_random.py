import random # import is how you tell python that you want to use a library in a script

# python convention: ALL_CAPS to indicate that a variable is a 'constant' that is easy to change
# in one place to alter the behavior of the script, but is NOT a variable that should
# be overwritten by other stuff when executing the script.
# NOTE: the ALL_CAPS will be important later when we discuss 'scope', but for
# now just trust me.
MAX_VALUE = 250

# this is calling the 'randint' function in the 'random' library
my_rand_int = random.randint(1, MAX_VALUE) # between the 1st argument and the 2nd, inclusive
print(f'my random integer: {my_rand_int}')

# the random library can do lots of other things, but involve data types
# and data structures that we'll get to soon.

print('') # print a blank line


my_rand_sum = random.randint(1, MAX_VALUE) + random.randint(1, MAX_VALUE)
print(f'Two random numbers from 1 to {MAX_VALUE} summed to {my_rand_sum}')


# <TRY IT OUT>
# # grab a random integer between 0 and 50


# # simulate rolling two 6-sided dice, print the result


# # a bit harder... roll two dice with random sizes!

