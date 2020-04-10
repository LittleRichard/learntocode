import random

# basic math stuff

my_var = 6 + 7
print(my_var) # 13

my_var = 13 - 8
print(my_var) # 5

my_var = 5 * 3
print(my_var) # 15

my_var = 15 / 4
print(f'15 / 4 is {my_var}')  # 3.75

# just showing you in case you ever need to debug this
my_var = 15 // 4  # // means 'integer division'
print(f'15 / 4 is {my_var}')  # 3, WTF this should be 15/4 = 3.75
# this has to do with the way python uses integers and floating point numbers
# an integer divided by an integer will return an integer, rounded down
# this is an oddity of python, just be aware of it

print('') # print a blank line to space out the output a bit

# there's one more basic math op that is handy, the 'modulus' AKA 'get remainder'
my_rem = 25 % 4  # 25 / 4 = 6 with a remainder of 1
print(f'25 divided by 4 has a remainder of {my_rem}')  # 1
my_rem = 100 % 4  # 100 / 4 = 25 with a remainder of 0
print(f'100 divided by 4 has a remainder of {my_rem}')  # 0

# don't forget order of operations!!!
# this is where code style becomes really important,
# and it's not just about the code working, but also making sure other
# people can read and understand it.

print('') # print a blank line

# PEMDAS!
# applied in order of multiplication, division, addition, subtraction
my_var = 2 * 3 + 10 / 5 - 3 # who knows what this equals, it's a mess
print(f'my_var 1 {my_var}')
# order of operations, this is equivalent to:
my_var = (2 * 3) + (10 / 5) - 3
print(f'my_var 2 (same as 1, with parentheses equivalent to PEMDAS) {my_var}')
# use parentheses to explicitly tell python what you want
my_var = (((2 * 3) + 10) / 5) - 3
print(f'my_var 3 (parentheses lead to different outcome) {my_var}')

print('') # print a blank line

# <TRY IT OUT>
# print how many times you can divide 100 by 3 EVENLY


# add 2, then multiply by 3


# print your result


# is it evenly divisible by 7? prove it

