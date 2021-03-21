# so far we have only worked with 3 datatypes:
# int
# str
# bool
# but what if we want to create a collection
# of these datatypes?
print("""
Lists and tuples are our first datastructures!  They are both
an ordered sequence of elements, where an element can be
any datatype or datastructure (even another list/tuple).

They can be used almost identically, with one key difference.
*** Tuples are immutable, lists can be modified. ***
""")

# create a tuple by separating the elements you want
# with commas, all inside parentheses:
my_first_tuple = (1, 2, 3, 4)
print(f'type {type(my_first_tuple)}, elements: {my_first_tuple}')

# a list can be declared the same way, but with square brackets
# instead of parentheses
my_first_list = [1, 2, 3, 4]
print(f'type {type(my_first_list)}, elements: {my_first_list}')

# because you can add elements to a list, they're more powerful,
# but you should use a tuple if you don't need to change it!!!

# you can put anything you want in a list or tuple, it's just a 
# data structure BUT BE CAREFUL, you have to live with 
# the data structures you create
a_terrible_tuple = (1, 2.0, '33333', my_first_tuple) 
print('a really badly designed tuple is on the next line:')
print(a_terrible_tuple)

print('')  # space out the output with a new line
 
# elements of the tuple are addressable and retrievable by 
# their 'index', or their location in the tuple's order.
print('In python, the index is ZERO-BASED')
print('This means that the first element is at index 0!')

# make a new tuple
american_stuff = ('baseball', 'hot dogs', 'apple pie')
print(f'american stuff: {american_stuff}')

# access the element of a tuple or list with square
# brackets and the index number
baseball_str = american_stuff[0]
hot_dog_str = american_stuff[1]
print(f'0th element is {baseball_str}')
print(f'1th element is {hot_dog_str}')
# access relative to the end with negative numbers
back_1 = american_stuff[-1]
back_2 = american_stuff[-2]
print(f'-1th element is {back_1}')
print(f'-2th element is {back_2}')

# accessing elements out-of-bounds will throw an error
# just print the bad code so we dont cause the script
# to fail and stop.
print("""
if you run this next statement:
    out_of_bounds = my_tuple[1000] # BOOOOM
you will see
>>> IndexError: tuple index out of range
""")

print('') # print a blank line for spacing

# let's make a tuple where the value is 1-based
one_to_ten = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# o2t is shorthad for one to ten
o2t_four = one_to_ten[4]
o2t_five = one_to_ten[5]
o2t_six = one_to_ten[6]
print(f'index 4-6 (zero based!): {o2t_four} {o2t_five} {o2t_six}')

# you can get the length of a tuple or list by using
# the `len` function, which is a built-in like print
length_one_to_ten = len(one_to_ten)
print(f'{length_one_to_ten} elements in {one_to_ten}')

# because of zero-based indexing, there will never
# be an element at the length! Always one fewer
if one_to_ten[length_one_to_ten - 1] == one_to_ten[-1]:
    print('This prints because it will always be true!')

print("""
Let's try lists now.
""")

# make an list with some values
small_list = [0, 1, 2 ,3]
print(f'starting list : {small_list}')

# because this is a list and not a tuple,
# we can change the values
small_list[0] = -10
small_list[-1] = 300
print(f'[0] = -10, [-1] = 300 : {small_list}')

# you can add an element to the end of a list
# using the `append` function
small_list.append(4)
small_list.append(5)
print(f'append(4), append(5) : {small_list}')


# TRY IT OUT

# define a tuple with 5 integers

# define a list with 5 integers

# compare the first element of the tuple
# to the final element of the list.
# print one thing if they're equal, and
# another if they're not.

print('You will see more with lists next.')
