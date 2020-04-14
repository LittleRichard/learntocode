import random

# let's explore a few more functions inside
# the `random` library. there are quite a few:
# https://docs.python.org/3.6/library/random.html

# if you want to drink from the fire hose, here
# is everything that comes standard in python.
# https://docs.python.org/3.6/library/
# for reference, i'm very familiar with about 
# a third of it, have used or am aware of another third, and
# can (mostly) infer what the rest does.

# back to the `random` library. the `choice` function 
# returns a random element from a "sequence", 
# defined as an ordered collection of data.
# we'll explore this more in the next script.

# luckily, python strings are sequences
# so we can experiment using a familiar data type.
print('a string is an ordered collection of characters.')

# TODO: define a string that you'll use with
# all your experiments with random.


# TODO: invoke the `choice` function from the
# `random` library to pick a character from your string.
# print the result.


# TODO: invoke the `sample` function to grab a random
# number of characters from your string in a random order:
# https://docs.python.org/3.6/library/random.html#random.sample

# can you figure out how to use the `sample` function to 
# return a shuffled version of the input? `random` has a shuffle function, 
# but sadly we can't use it with strings (we'll learn why next class!)
# the `len` function might be helpful here, punch it into google.


# why does this print funny with the square brackets
# and commas? this is a data type we haven't seen yet,
# and is up next! here's some code to adjust it so it
# prints nicely, by joining all the elements in your
# sample together with an empty string between each. 
nice_print = ''.join(your_sample)
print(nice_print)


# TODO: make a password generator.  
# does it create a good password or not, and why?
# how can you make it generate better passwords?


# if you're bored: can you make it create a password 
# based on how strong your user wants it to be?


# if you did it successfully, you have reached
# feature parity with multiple (free) apps in your
# phone's app store that have 100s of thousands of
# downloads collectively. Not bad for a couple weeks!
