import time
import random

# in the bonus_more_random script, we saw that strings
# can be used as sequeneces, here it is again:
definition_string = 'a string is an ordered collection of characters.'
print(definition_string)
def_string_length = len(definition_string)
print(f'length of this string is {def_string_length}')

# this is a for-loop, it executes as follows:
## 1. The 'element' variable is assigned the next value from the iterable
##    BUT, if there are no more values in the iterable, the loop breaks 
##    and no more of the indented code is executed.
## 2. The indented code is executed
## 3. return to #1 
print('** debug ** before first for loop')

for current_value in 'abcd':
    print(f'current_value from abcd: {current_value}')

# printing directly before and directly after
# a block of code you're curious about can help
# you isolate it
print('** debug **: after first for loop')

# you can also iterate over a string in a variable
iter_string = 'hello world'
for curr_val in iter_string:
    print(f'hello world: {curr_val}')

# a `range` is special type of iterable that, when looped over,
# will give you sequential values in a pattern.
# a simple range will have the given number of elements,
# as integers from 0 to length-1
my_range = range(7)
print(f'range(7) printed out: {my_range}')

# but most commonly you'll just use them directly 
# as you declare your loop.
for index_num in range(7):
    print(f'range(7): {index_num}')

print('') # blank line

# range(X, Y) will yield the values: X, X+1, X+2 ..., Y-2, Y-1
# NOTE: the difference between X and Y is the length
# NOTE: Y must be greater than X or you'll get an empty iterable
for x in range(3, 10):
    print(f'xrange(3, 10) current value is {x}')

print('') # blank line

# with 3 arguments: (start, end, step_size)
for x in range(0, 12, 3):
    # by steps of 3
    print(f'range(0, 12, 3): {x}')

# backward: (start, end, negative_step_size)
for x in range(12, 0, -1):
    print(f'range(12, 0, -1): {x}')


# keep track of things you find
div1 = 211
div2 = 837
max_div_both = 0  # initialize this to 0
for x in range(1000000):

    # remember the mod operator? 
    # returns zero if the value is evenly divisible
    if (x % div1 == 0) and (x % div2 == 0):
        max_div_both = x

# at the end of the loop, our variable
# tracking the max holds the answer
print(f'found it! {max_div_both}')


# TRY IT OUT

# # sum the numbers 1 through 1000


# # print every possible combination of rolling 2 6-sided dice
# # hint: what happens if you put a for loop INSIDE a for loop?


# and now let's make a good password generator
char_pool = 'abcdefghijklmnopqrstuvwxyz,./;!@#$%^&*()-+_='

pw_length = input('how long password? ')
pw_length = int(pw_length)
if pw_length < 12:
    print(f'{pw_length} is too short, you get 12')
    pw_length = 12

user_pw = ''
for x in range(pw_length):
    # here we dont actually care about x, we're
    # including it because for-loop syntax requires
    # something to hold the current iteration variable.

    user_pw = user_pw + random.choice(char_pool)

# each loop selected a random character independently!
print(f'user password: {user_pw}')
