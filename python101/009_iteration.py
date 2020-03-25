import time
import random

# make an iterable (in this case a tuple) with some values
# this is a for-loop, it executes as follows:
## 1. The 'element' variable is assigned the next value from the iterable
##    BUT, if there are no more values in the iterable, the loop breaks 
##    and no more of the indented code is executed.
## 2. The indented code is executed
## 3. return to #1
my_tuple = (1, 2, 3, 4, 5, 6) 
for my_element in my_tuple:
    print('my_element from my_tuple: %s' % my_element)

# xrange returns a special type of iterable that doesn't retain any history of what WAS in it,
# which makes it much more efficient in memory for large iterables
# tuple(xrange(X)) takes the output of the xrange and turns it into a tuple
my_tuple_from_xrange = tuple(xrange(7))
print(my_tuple_from_xrange)

print('') # blank line

# xrange(X) will yield the values: 0, 1, 2, 3, ..., X-2, X-1
# NOTE: the X you provide is the length, NOT the maximum value (because it's zero-based!)
for x in my_tuple_from_xrange:
    print('xrange(7) current value is : %s' % x)

print('') # blank line

# xrange(X, Y) will yield the values: X, X+1, X+2 ..., Y-2, Y-1
# NOTE: the difference between X and Y is the length
# NOTE: Y must be greater than X or you'll get an empty iterable
my_tuple_from_xrange = tuple(xrange(3, 10))
for x in my_tuple_from_xrange:
    print('xrange(3, 10) current value is : %s' % x)

print('') # blank line

# because the xrange is also iterable, you
# can use it directly without pulling it into a tuple first.
for x in xrange(3, 10):
    print('xrange(3, 10) used directly current value is : %s' % x)

# confirm by:
## iterate 10 times, printing the number of each iteration
for x in xrange(1, 11): 
  print('xrange(1, 11) current value is : %s' % x)

print('')

## print every possible combination of rolling 2 6-sided dice
## hint: use 2 for-loops!
for dice_one in xrange(1,7):
    for dice_two in xrange(1,7):
        print('%s and %s totals %s' % (dice_one, dice_two, dice_one + dice_two))


# MORE xrange TECHNIQUES
# we won't use them heavily, but it's nice to know they're there
HIDE_EXTRA = True # flip me to False to avoid exiting
if HIDE_EXTRA:
    exit() # exits script immediately.
print('')
print('Extra techniques')
print('')

# to go backwards, we must also specify a 'step size'
# Think of this as: 'I want every Nth value between X and Y, inclusive of X but exclusive of Y'
# xrange(X, Y, N)
my_tuple_from_xrange = xrange(10, 3, -1) # can just use an xrange directly here
for x in my_tuple_from_xrange: 
    print('xrange(10, 3, -1) current value is : %s' % x)

print('') # blank line

# BE CAREFUL with your step sizes, will only use values less than (and never equal to)
# the 'end' value; REMINDER: inclusive of X but exclusive of Y
for x in xrange(3, 10, 5): 
    print('xrange(3, 10, 5) current value is : %s' % x)