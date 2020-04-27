import random
import string

# for loops and while loops are both forms
# of iteration, but 95% of the time your logic
# and data processing will be over finite
# data, and...
print("""
    some more ways to loop over finite data structures
    most of these will work with both tuples and lists,
    the ways that wont work are (probably) because of
    mutability; lists can change and tuples cant.
""")

# declaring tuples
# instead of typing (0, 1, 2, 3, 4)
tuple_ten = tuple(range(10))
print(f'tuple_ten {tuple_ten}')

list_ten = list(range(10))
print(f'list_ten {list_ten}')

# this is a python "idiom" called a list comprehension
# it for-loops in place to yield each element of 
# tuple_ten, as x, to the list creation function
list_comp = [x for x in tuple_ten]
print(f'list_comp {list_comp}')

# [x for x in y] means list
# (x for x in y) doesnt mean a tuple...
# tuple(x for x in y) means a tuple

# you can do this with tuples too, but
# for whatever reason its never called a 
# tuple comprehension.

# you can do whatever you want with the first 
# this could be a way of gradually increasing the 
# likelihood of something?
print("""
    the first x in "x for x" is what goes in the list, 
    the " for x in " will never change. instead of the 
    first x, try something more complicated
""")
random_ints = [random.randint(x, x + 10) for x in range(15)]
print(f'random_ints {random_ints}')

print('')

# sort a list
sorted_rand_ints = sorted(random_ints)
print(f'sorted_rand_ints {sorted_rand_ints}')

# reverse a list or tuple without changing it
reversed_sorted = reversed(sorted_rand_ints)
print(f'reversed_sorted {reversed_sorted}')
print(f'    wait what? reversed() returns a thing like a range')
reversed_sorted_list = list(reversed(sorted_rand_ints))
print(f'reversed_sorted_list {reversed_sorted_list}')

# sort and reverse at the same time!
sort_rev_one_step = sorted(random_ints, reverse=True)
# we'll come back to the `reverse=True` later, it's
# called a 'keyword argument', AKA a 'kwarg'
print(f'sort_rev_one_step    {sort_rev_one_step}')

print('')

# this for-loop...
div_by_13_for_loop = []
for x in range(200):
    if x % 13 == 0:
        div_by_13_for_loop.append(x)

# is equivalent to:
div_by_13 = [x for x in range(200) if x % 13 == 0]
# ^^^ this idiom is not only convenient, but 
# for bits & bytes reasons it is WAY faster
# the bits and bytes: 
# memory allocation of a list as it grows one element
# at a time is expensive, but the list comprehension
# sizes the whole list all at once.

if div_by_13 == div_by_13_for_loop:
    print('for-loop/append == list_comp')

# search for one of a group of values!
look_for = (51, 52, 53)

# iterate over a list
for x in div_by_13:
    print(f'{x} is divisible by 13')

    # use the 'in' keyword to return True
    # if the first value is present in the 2nd
    # value
    if x in look_for:
        print(f'*** {x} is in {look_for}')

print('')

# TRY IT OUT
char_pool = string.ascii_letters

# grab 25 characters from your pool, with re-use!

# count how many of them are the letter a
# hint: the 'len' function might help you here

# do it again but look for ABCabc
# hint: use an 'in' statement in a list comprehension
