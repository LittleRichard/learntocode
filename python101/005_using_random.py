# python comes with a lot of 'built-in' libraries.  Libraries typically
# focus on a topic, and many of them rely on each others' tools. In this
# case it's a core python library, but eventually you can install
# and use anyone's to do whatever you need.
import random # import is how you tell python that you want to use a library in a script

# python convention: ALL_CAPS to indicate that a variable is a 'constant' that is easy to change
# in one place to alter the behavior of the script, but is NOT a variable that should
# be overwritten by other stuff when executing the script.
# NOTE: the ALL_CAPS will be important later when we discuss 'scope', but for
# now just trust me.
MAX_VALUE = 250

# this is how you access the 'randint' function in the 'random' library, 
# which we can print out just like any other variable.
print(f'Next line will look weird. random.randint is a reference to:')
print(random.randint)

# if instead of using it as a variable, we can 'invoke' it as 
# a function, sometimes also called a method, 
# by putting (<arguments to the function>) after it.
my_rand_int = random.randint(1, MAX_VALUE) # between the 1st argument and the 2nd, inclusive
print(f'my random integer: {my_rand_int}')

# this is exactly what we've been doing with 'print' this whole time!
print(f'print function as variable: {print}')
# your code editor probably colored the {print} differently... it's just
# confused, you can ignore it.

# Later: we will learn about functions soon, but for now they're just
# tools in your toolbox.
print('We will learn more about functions later')


# the random library can do lots of other things, but involve data types
# and data structures that we'll get to soon.

print('') # print a blank line

# to save space and variables, use values you will throwaway 'in-line'
# and only put the result in a variable.
my_rand_sum = random.randint(1, MAX_VALUE) + random.randint(1, MAX_VALUE)
print(f'Two random numbers from 1 to {MAX_VALUE} summed to {my_rand_sum}')


# <TRY IT OUT>
# # grab a random integer between 0 and 50


# # simulate rolling two 6-sided dice, print the result


# # a bit harder... roll two dice with random sizes!

