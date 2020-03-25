import random

# basic math stuff

my_var = 6 + 7
print(my_var) # 13

my_var = 13 - 8
print(my_var) # 5

my_var = 5 * 3
print(my_var) # 15

my_var = 15 / 4
print('15 / 4 is %s ' % my_var) # 3, WTF this should be 15/4 = 3.75
# this has to do with the way python uses integers and floating point numbers
# an integer divided by an integer will return an integer, rounded down
# this is an oddity of python, just be aware of it

print('') # print a blank line

# if at least one of the two values is a float, works as expected and returns a float
my_var = 15.0 / 4
print('15.0 / 4 is %s' % my_var) # 3.75

print('') # print a blank line

# there's one more basic math op that is handy, the 'modulus' AKA 'get remainder'
# sadly, it uses the same character as our 'interpolation', which is confusing.
my_rem = 25 % 4 # 25 / 4 = 6 with a remainder of 1
print('25 divided by 4 has a remainder of %s' % my_rem) # 1
my_rem = 100 % 4 # 100 / 4 = 25 with a remainder of 0
print('100 divided by 4 has a remainder of %s' % my_rem) # 0

# don't forget order of operations!!!
# this is where code style becomes really important,
# and it's not just about the code working, but also making sure other
# people can read and understand it.

print('') # print a blank line

# applied in order of multiplication, division, addition, subtraction
my_var = 2 * 3 + 10 / 5 - 3 # who knows what this equals, it's a mess
# order of operations, this is equivalent to:
my_var = (2 * 3) + (10 / 5) - 3
# use parentheses to explicitly tell python what you want
my_var = (((2 * 3) + 10) / 5) - 3

print('') # print a blank line

# confirm by:
# print how many times you can divide 100 by 3 evenly
my_int = 100 / 3
print(my_int) # integer division!
# add 2, then multiply by 3
my_int = (my_int + 2) * 3
# print your result
print('my modified integer is %s ' % my_int)
# is it evenly divisible by 7? how could you tell?
print(my_int % 7)