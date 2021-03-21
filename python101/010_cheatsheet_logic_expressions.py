print('a series of quick examples demonstrating common logic tests')

# this script isn't designed to do anything, just show
# some examples as a reference. we won't cover it in class

print('all of these statements return a boolean, for example: ')
one_equal_two = 1 == 2  # a little goofy looking, but valid
print(f'one_equal_two {one_equal_two}')

# comparison operators
if 1 > 0:
    print('>')

if 1 >= 0:
    print('>=')

if -1 < 0:
    print('<')

if -1 <= 0:
    print('<=')

if 1 == 1:
    print('==')

if 2 != 1:
    print('!=')

# == and != also work with tuples/lists
# by checking each index iteratively,
if (1, 2, 3) == (1, 2, 3):
    print('tuple == tuple')

# but a list will never equal a tuple because they're
# different data types, even if the contents are the same.
if (1, 2, 3) != [1, 2, 3]:
    print('list != tuple')

x = 10
# check containment against a tuple by iterating
# over the tuple until a match is found
if x in (1, 2, 3, 10, 11):
    print('in tuple')

# 'not in' works too
if x not in (1, 2, 3):
    print('not in tuple')

# check containment against a string
x = ' abc '
if x in 'asdfas abc dfdasfsad':
    print('string in string')

# string starts with
my_str = 'abcdefghi'
if my_str.startswith('abc'):
    print('.startswith()')

# string ends with
if my_str.endswith('i'):
    print('.endswith()')

# lots of and/or, make sure you use () to
# tell python explicitly what you want for
# order of operations!
x = 10
if (x in (1, 2, 3) or x in (8, 9, 10)) and x < 20:
    print('nested and/or')
