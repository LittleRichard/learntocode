import random 

# lists work in almost the exact same way as tuples, except they're MUTABLE
# lists use square brackets, where tuples use parentheses
my_list = [0,1,2,3,4]
my_tuple_from_list = tuple(my_list) # create a tuple from the elements of my_list
my_list_from_tuple = list(my_tuple_from_list)

# for all the stuff about indices, index-based-access, slicing, and printing, see
# the lesson on tuples.

# LISTS ARE MUTABLE, and this is simultaneously useful and dangerous
my_list[3] = 99 # sets the element at index 3 (the 4th position)
print('my list now:  %s ' % my_list)

# a more interesting case
my_other_list = my_list
my_list[1] = 7
print('my list       %s' % my_list) # see the 7 we just changed and the 99 from earlier
print('my other list %s' % my_other_list) # modifying 'my_list' modified my_other_list
# WTF these are different variables?!??!?!
# yes, but variables are just labels.  in this case, both labels are referencing 
# the same list in your computer's memory (RAM), so when you modify one you modify both
print('it is so important that you remember this behavior!!!!')
# this is why tuples are nice; they're immutable so it's
# impossible to ever get yourself in trouble this way.

if my_list == my_other_list: # test for equality between two lists
    print('these two lists have the same values at the same indexed locations')

if my_list is my_other_list: # test that these variables represent the same object
    print('these two lists are the SAME list')

print('')

my_copy_list = list(my_list) # this creates a new list full of the same values as the original
assert my_copy_list == my_list # still equal
assert my_copy_list is not my_list # equal, but not the same exact object
print('passed assertions without failing, lists are not the same list because it was copied')

my_copy_list[0] = 8
print('my_list        %s' % my_list) # no 8s here
print('list(my_list)  %s' % my_copy_list) # 8 is in this one
print('')

# WARNING, this is about to get really weird, but after you get through it
# all the stuff you'll use much more frequently is pretty easy.

# one more subtlety with multi-dimensional lists
my_2d_list = [
              [1,2,3], # my_2d_list[0][0:2]
              [4,5,6], # my_2d_list[1][0:2]
              [7,8,9], # my_2d_list[2][0:2]
              ]

for outer_list in my_2d_list:
    print('outer %s' % outer_list)
    for element in outer_list:
        print('element %s' % element)

my_copy_2d_list = list(my_2d_list)
my_2d_list[1][1] = 99 # the middle element of this 3x3 array gets 99
print('original (directly modified) 2d list middle element is %s' % my_2d_list[1][1])
print('copy of 2d list middle element is %s' % my_copy_2d_list[1][1])
# waaaaat the copy's [1][1] element is also changed??????
# this is because the list(my_2d_list) makes a copy of the OUTER list (the one that
# holds 3 lists), but it copies ONLY THE REFERENCES to the inner lists. So like in the 
# example above, when we change the inner list
# it modifies the inner list inside the copy as well!

# Confused? I was too, don't worry about it too much except being aware
# that you have to be REALLY CAREFUL anytime you make a copy of a list.
# to learn about copying lists to handle this, uncomment below,
# but we're going to skip it because it's not commonly useful.
# it's also generally a bad approach because it's slow
# if it's a key part of your algorithm.
import copy # a library specifically to handle stuff like this
DEMO_COPY = False
if DEMO_COPY:
    my_2d_list[1][1] = 1234
    my_other_copy_2d_list = copy.copy(my_2d_list) # equivalent to the list thing we did above, handles infinite dimensions!
    my_deep_copy_2d_list = copy.deepcopy(my_2d_list) # a true copy of all innards, handles infinite dimensions!
    my_2d_list[1][1] = 9876 # the middle element of this 3x3 array gets 99
    print('original (directly modified) 2d list middle element is %s' % my_2d_list[1][1])
    print('the copy.copy() of the 2d list middle element is %s' % my_other_copy_2d_list[1][1])
    print('the copy.deepcopy() of 2d list middle element is %s' % my_deep_copy_2d_list[1][1])
    print('')

# NO MORE BITS AND BYTES for the rest of this script.

# you can do more than just change values in a list, you can add stuff to them
# append adds a single element to the end
new_list = [0] # a list with 1 element!
print('new list %s' % new_list)
new_list.append(1) # call new_list's append function
new_list.append(2)
print('new list appended %s' % new_list)

# extend adds another list to the end
new_list2 = [5,7,8,9]
new_list.extend(new_list2)
print('new list extended %s' % new_list)

# removing elements is generally not a good idea for performance reasons
## bits and bytes: python needs to re-allocate memory space dynamically, can be slow.
# find and remove the first element matching the given value 
# (searching from index 0->end)
new_list.remove(5) 
# there is a far better data structure for doing this, called a set,
# which we haven't seen yet.
print('new list post-remove %s' % new_list)

# pull the element at the given index out of the list
# this is really slow because of bits-and-bytes 'memory allocation', 
# so beware
popped_element = new_list.pop(4) 
print('new list popped %s out of %s' % (popped_element, new_list))

# need to append to the beginning? use a different data structure, or
# think about how you can reverse your list at the end of your algorithm
# and append until reversing at the end.

# sorting is a really common thing to do with lists,
# but it can get complicated when you want to do a customized
# sort.  The 'sorted' built-in function takes an iterable and returns
# a sorted list.  It does NOT sort the list you give it in-place, it
# always creates a new one.
# Here's the simple case:
my_random_list = []
for x in xrange(10):
    my_random_list.append(random.randint(1,100))
my_sorted_list = sorted(my_random_list)
print('random list: %s' % my_random_list)
print('sorted list: %s' % my_sorted_list)
print('')

literature_names = ['Great Gatsby',
                    'For Whom the Bell Tolls',
                    'Beowulf',
                    'Dracula',
                    'Moby Dick']
sorted_lit_names = sorted(literature_names)
# there is an optional keyword argument 'reverse' that is a 
# boolean whether or not the list should be reversed. defaults to False
reversed_lit_names = sorted(literature_names, reverse=True)
print('lit: %s' % literature_names)
print('sorted lit: %s' % sorted_lit_names)
print('reversed lit: %s' % reversed_lit_names)

# and finally, if you want to sort on something other than
# numerical or alphabetical order, you can define a 'key'
# for the sorted function.
sorted_by_length_lit_names = sorted(literature_names, key=len) # our friend the len() function
print('sorted by length lit: %s' % sorted_by_length_lit_names)
# you can pass a function (in this case, the length function), which
# takes a single argument and returns a value that IS sortable numerically/alphabetically
# len returns the length of the string as a number, so this sorted list
# will be sorted by the length of each book name.

# you can also define your own functions for sorting
# this one makes sure that Dracula is always first,
# so it's kind of silly, but once you're in this function
# you can pretty much do anything.
def my_sort_function(my_string):
    assert isinstance(my_string, str)

    if my_string == 'Dracula':
        return 9999999 # an arbitrarily large number
    else:
        return len(my_string)

dracula_last_sorted_lit = sorted(literature_names, key=my_sort_function)
print('Dracula last: %s' % dracula_last_sorted_lit)