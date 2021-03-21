import random

# let's explore a few more functions inside
# the `random` library. there are quite a few:
# https://docs.python.org/3.6/library/random.html

# if you want to drink from the fire hose, here
# is everything that comes standard in python.
# https://docs.python.org/3.6/library/
# for reference, i'm very familiar with about 
# a third of it, have used another third, and
# can mostly infer what the rest does.

# back to the `random` library. the `choice` function 
# returns a random element from a "sequence", 
# defined as an ordered collection of data.
# we'll explore this more in the next script.

# luckily, python strings are sequences
# so we can experiment using a familiar data type.
print('a string is an ordered collection of characters.')

# TODO: define a string that you'll use with
# all your experiments with random.
my_str = 'abcdefghijklmnopqrstuvwxyz'


# TODO: invoke the `choice` function from the
# `random` library to pick a character from your string.
# print the result.
one_char = random.choice(my_str)
print(f'one char is: {one_char}')

# TODO: invoke the `sample` function to grab a random
# number of characters from your string in a random order:
# https://docs.python.org/3.6/library/random.html#random.sample
sample_str = random.sample(my_str, 10)

# can you figure out how to use the `sample` function to 
# return a shuffled version of the input? `random` has a shuffle function, 
# but sadly we can't use it with strings (we'll learn why next class!)
# the `len` function might be helpful here, punch it into google.
full_shuffle = random.sample(my_str, len(my_str))

# why does this print funny with the square brackets
# and commas? this is a data type we haven't seen yet,
# and is up next! here's some code to adjust it so it
# prints nicely, by joining all the elements in your
# sample together with an empty string between each. 
nice_print = ''.join(sample_str)
print(nice_print)


# TODO: make a password generator.  
# does it create a good password or not, and why?
# how can you make it generate better passwords?
char_pool = 'abcdefghijklmnopqrstuvwxyz,./;<>?:!@#$%^&*()'

# too short
weak_pw = random.sample(char_pool, 8)
weak_pw = ''.join(weak_pw)
print(f'this is too short to be good: {weak_pw}')

# this would be a good password, except
# the shuffle only uses each character once
# so there are FAR fewer combinations than 
# if re-use was possible. 
ok_pw = random.sample(char_pool, 16)
print(f'a bit better: {ok_pw}')

# same problem of no re-use, but at least
# this is long enough that it would take
# a while to brute-force it.
acceptable_pw = random.sample(char_pool, len(char_pool))

# if you're bored: can you make it create a password 
# based on how strong your user wants it to be?

# hopefully you did some googling and found many ways, but
# using the string library seems the most efficient to me

# this should at the top for style reasons, but python doesnt care
import string

# also, you can add strings together to concatenate them
added_strings = 'abc' + 'def'
print(f'2 strings added: {added_strings}')

pw_length = input('Enter password length: ')
pw_length = int(pw_length)

pw_complex = input('Enter complexity, 1-5: ')
pw_complex = int(pw_complex)

# these are separate events because we want 
# the cases to add up, so multiple if-trees instead
# of only one.
user_pw_char_pool = ''  # start with empty string

if pw_complex >= 1:
    user_pw_char_pool = user_pw_char_pool + string.ascii_lowercase

if pw_complex >= 2:
    user_pw_char_pool = user_pw_char_pool + string.ascii_uppercase

if pw_complex >= 3:
    user_pw_char_pool = user_pw_char_pool + string.digits

if pw_complex >= 4:
    user_pw_char_pool = user_pw_char_pool + string.punctuation

if pw_complex >= 5:
    # add these same characters several times to get 
    # an approximation of re-use
    user_pw_char_pool = (user_pw_char_pool 
                         + user_pw_char_pool
                         + user_pw_char_pool
                         + user_pw_char_pool
                         + user_pw_char_pool)

user_pw = random.sample(user_pw_char_pool, pw_length)
user_pw = ''.join(user_pw)
print(f'Your password is: {user_pw}')


# if you did it successfully, you have reached
# feature parity with multiple (free) apps in your
# phone's app store that have 100s of thousands of
# downloads collectively. Not bad for a couple weeks!
