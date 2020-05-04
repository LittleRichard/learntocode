
# remember how lists are 'mutable'?
# this renders a dangerous and powerful property,
# which is that variables holding lists are actually
# holding a REFERENCE to a list and not the list itself

int_ref_one = 100
int_ref_two = int_ref_one
int_ref_two += 1
print(f'int ref one, two : {int_ref_one} {int_ref_two}')

list_ref_one = [1, 2, 3, 4]
list_ref_two = list_ref_one
list_ref_two.append(5)
print(f'list_ref_two is as we would expect: {list_ref_two}')
print(f'list_ref_one is matches the other : {list_ref_two}')

print("""
Try to think of variables and data like lockers.

A locker has a number, which represents it's physical location.

A locker can be 'labeled' with a name, so that
anything with that label should go in the locker. However,
labels can move to different lockers over time, or can
even have multiple labels for the same locker.

For immutable datatypes, modifying the contents of the locker
will create a new piece of data and put it in a different locker
(even if the new locker still has the same label).

For mutable datatypes, modifying the contents of the locker
is totally fine. Any label that finds the locker will open
it and find the modified contents!
""")

# this behavior crosses function scope, because
# you're providing the LABEL for the locker holding
# the data. so if it modifies the contents, you can
# see it outside scope!!!
def append_a_list(my_list, element):
    my_list.append(element)
    return my_list

first_list = [1, 2, 3]
print(f'first_list pre : {first_list}')
appended_list = append_a_list(first_list, 4)
print(f'first_list post: {first_list}')
print(f'appended_list  : {appended_list}')

print('')

# python can help you out with the 'is' comparison,
# which is a layer deeper than element-wise equality

new_list = [1, 2, 3, 4]
if new_list == first_list:
    print('new_list == first_list')

# we'll use 'is not' so that we see the print
if new_list is not first_list:
    print('new_list is not first_list')

if first_list is appended_list:
    print('first_list is appended_list')

print('again, this is useful and dangerous!!!')
print('it is important to know this to avoid bugs')