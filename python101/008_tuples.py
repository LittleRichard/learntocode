
yard_base_str = 'My %s brings all the %s to the yard'

# so far we've worked with integers (int), floats (float), and strings (str)
# but we've actually used tuples already, you just didn't know it
print(yard_base_str % ('milkshake', 'boys'))

# tuples are defined using parentheses, with each element separated by a comma
# a tuple is an ordered collection of things, and is IMMUTABLE,
# a sciency word meaning it can't be modified
my_tuple = ('milkshake', 'boys') # defines a tuple with 2 elements
print(yard_base_str % my_tuple) # equivalent to print statement above!

# you can put anything you want in a tuple, it's just a data structure
# BUT BE CAREFUL, you have to live with the data structures you create
my_mixed_up_tuple = (1, 2.0, '33333', yard_base_str, tuple) 
# tuples can be printed using '%s', because tuples have a built-in
# way of converting themselves to strings
print(my_mixed_up_tuple)

# elements of the tuple are addressable and retrievable by their index
# Index is ZERO-BASED.  This means that the first element is at index 0, 2nd at 1...
# use the syntax: >>> the_tuple[INDEX_INTEGER]
milkshake_str = my_tuple[0]
boys_str = my_tuple[1]
print('0th element is %s' % milkshake_str)
print('1th element is %s' % boys_str)


# accessing elements out-of-bounds will throw an error
print('the next statement will throw an error')
# sout_of_bounds = my_tuple[1000] # BOOOOM
# >>> IndexError: tuple index out of range

# or, if you know the shape of your tuple, you can unpack it directly
# this looks goofy... but think of as an extension of a normal variable assignment statement
my_tuple = ('milkshake', 'boys')
(milkshake_str, boys_str) = my_tuple
print(yard_base_str % (milkshake_str, boys_str))

print('') # print a blank line

# you can also 'slice' a tuple
new_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print('there are %s elements in %s' % (len(new_tuple), new_tuple))
my_slice = new_tuple[4:7] # grabs the elements from index 4 thru index 7. DOES NOT grab new_tuple[7]

# print('Slice 1 is %s' % my_slice) 
# the line above throws an error, because the dynamic printing 
# is looking for a %s corresponding to each element of my_slice

print('Slice [4:7] by index: %s %s %s' % (my_slice[0], my_slice[1], my_slice[2]))
# (some_variable,) is how you define a tuple with 1 element
print('Slice [4:7] as tuple: %s' % (my_slice,)) 

# this is weird! 
tuple_of_a_tuple = (my_slice,)
print('tuple of a tuple below:')
print(tuple_of_a_tuple) # ( (0,1,2), ) # see the inner and outer tuple?

# retrieve tuple length using the builtin python function 'len'
tuple_length = len(my_tuple)

# a way to retrieve the final element of a tuple
## see bottom of script for advanced slicing
final_element = my_tuple[tuple_length - 1] # -1 because zero-based
print('final element is %s' % final_element)

# another way to do this is using negative index values
print('final element is %s' % my_tuple[-1])
# think about this as the index walking backwards from the end,
# EXCEPT that there is not a 'negative zero' index

# tuples are IMMUTABLE; you can't alter the contents or add stuff
# my_tuple[0] = 'root beer float' # BOOOOM
# >>> TypeError: 'tuple' object does not support item assignment

print('') # print a blank line

# confirm by:
## declare a tuple with 6 elements
my_tuple = (0, 1, 2, 3, 4, 5)
## print the first two elements and the last element
print('first two elements: %s %s.  last element: %s' % (my_tuple[0], my_tuple[1], my_tuple[-1]))
## can you do it using only two template values?
print('first two elements: %s.  last element: %s' % (my_tuple[0:2], my_tuple[-1]))
## print its length
print('my tuple has %s elements' % len(my_tuple))





# MORE SLICING TECHNIQUES
# we won't use them heavily, but it's nice to know they're there
HIDE_EXTRA = True # flip me to False to avoid exiting
if HIDE_EXTRA:
    exit() # exits script immediately.
print('')
print('Extra techniques')
print('')


slice_from_start = new_tuple[:3] # grabs everything from the beginning up to 3. DOES grab new_tuple[3]
print('slice [:3] is %s' % (slice_from_start,))
slice_to_end = new_tuple[3:] # same thing, grabs the value at index 3 to the end
print('slice [3:] is %s' % (slice_to_end,))
slice_out_of_bounds = new_tuple[4:1000] # python is forgiving and only goes to the end
print('slice [4:1000] is %s' % (slice_out_of_bounds,))

print('') # print a blank line

# negative indices are a convenience, python uses them
# to mean 'backwards from the end of the tuple'
element_from_end = new_tuple[-2]
print('2nd to last element is %s' % element_from_end)

# slice all except the first and last
the_middle = new_tuple[1:-1]
print('the middle is %s' % (the_middle,))

# slice using all negative indices
another_middle = new_tuple[-4:-1]
print('another middle is %s' % (another_middle,))

print('') # print a blank line